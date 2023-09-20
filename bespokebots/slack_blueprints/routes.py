from flask import Blueprint, jsonify, request, session, redirect, url_for, make_response
from flask import Response
from flask import current_app as flask_app
import html
import json
import os
import uuid
import logging
from slack_bolt import App, Ack
from slack_sdk.oauth import AuthorizeUrlGenerator
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk.web import WebClient
from bespokebots.services.celery_tasks import slack_app, process_slack_message, slack_env_vars
from bespokebots.dao.database import db
from bespokebots.dao import ServiceProviders, OAuthStateToken


logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)


slack_bp = Blueprint("slack", __name__)
handler = SlackRequestHandler(slack_app)



# slack OAuth handling starts here
@slack_bp.route("/services/oauth/slack/connect", methods=["GET"])
def oauth_connect_slack():
    from bespokebots.services.user_service import UserService
    
    user_service = UserService(db.session)
    user_id = session.get("user_id")
    logger.info(f"Slack OAuth connect request received for user_id: {user_id}")

    if not user_id:
        return make_response("No user_id in session, please log in first", 400)
    
    user = UserService.lookup_by_user_id(user_id) if user_id else None
    client_id = slack_env_vars.get("client_id")
    scope = slack_env_vars.get("bot_scopes")
    logger.info(f"Configured bot scopes: {scope}")
    user_scopes = slack_env_vars.get("user_scopes")
    logger.info(f"Configured user scopes: {user_scopes}")
    state = user_service.create_state_token(user.id)
    redirect_uri = url_for("slack.oauth_callback_slack", _external=True)
    authorize_url = AuthorizeUrlGenerator(
        client_id=client_id,
        scopes=scope,
        user_scopes=user_scopes,
        redirect_uri=redirect_uri,
    ).generate(state.value)

    logger.info(f"Generated authorize_url: {authorize_url}")
    user_service.initialize_user_credentials(
        user,
        ServiceProviders.SLACK.value,
        service_user_id="not_yet_activated",
        state_token=state,
    )
    logger.info(f"UserCredentials record created for user_id: {user.id}, redirecting use to Slack's authorize_url")
    return redirect(authorize_url)


@slack_bp.route("/services/oauth/slack/callback", methods=["GET"])
def oauth_callback_slack():
    from bespokebots.services.user_service import UserService
    logger.info("Slack OAuth callback request received")
    user_service = UserService(db.session)
    client_id = slack_env_vars.get("client_id")
    client_secret = slack_env_vars.get("client_secret")
    redirect_uri = url_for("slack.oauth_callback_slack", _external=True)
    state = request.args.get("state")
    user = user_service.lookup_user_by_state_token(state)
    logger.info(f"Slack OAuth callback with State: {state} received for user_id: {user.id}")
    
    if "code" in request.args:
        # Verify the state parameter
        logger.info(f"Slack OAuth callback, validating state token: {state}")
        if user_service.validate_state_token(request.args["state"]):
            client = WebClient()  # no prepared token needed for this
            # Complete the installation by calling oauth.v2.access API method
            logger.info(f"Slack OAuth callback, retrieving access token from slack for user_id: {user.id} with oauth state token: {state}")
            oauth_response = client.oauth_v2_access(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                code=request.args["code"],
            )
            logger.info(f"Slack OAuth callback, successfully retrieved oauth response from slack for user_id: {user.id} with oauth state token: {state}")
            # pull out the Slack specific fields to encrypt as the
            # credentials object in the UserCredentials record
            installed_enterprise = oauth_response.get("enterprise") or {}
            is_enterprise_install = oauth_response.get("is_enterprise_install")
            installed_team = oauth_response.get("team") or {}
            installer = oauth_response.get("authed_user") or {}
            incoming_webhook = oauth_response.get("incoming_webhook") or {}
            bot_token = oauth_response.get("access_token")
            # NOTE: oauth.v2.access doesn't include bot_id in response
            bot_id = None
            enterprise_url = None
            if bot_token is not None:
                auth_test = client.auth_test(token=bot_token)
                bot_id = auth_test["bot_id"]
                if is_enterprise_install is True:
                    enterprise_url = auth_test.get("url")

            installation_credentials = {
                "app_id": oauth_response.get("app_id"),
                "enterprise_id": installed_enterprise.get("id"),
                "enterprise_name": installed_enterprise.get("name"),
                "enterprise_url": enterprise_url,
                "team_id": installed_team.get("id"),
                "team_name": installed_team.get("name"),
                "bot_token": bot_token,
                "bot_id": bot_id,
                "bot_user_id": oauth_response.get("bot_user_id"),
                "bot_scopes": oauth_response.get("scope"),  # comma-separated string
                "user_id": installer.get("id"),
                "user_token": installer.get("access_token"),
                "user_scopes": installer.get("scope"),  # comma-separated string
                "incoming_webhook_url": incoming_webhook.get("url"),
                "incoming_webhook_channel": incoming_webhook.get("channel"),
                "incoming_webhook_channel_id": incoming_webhook.get("channel_id"),
                "incoming_webhook_configuration_url": incoming_webhook.get(
                    "configuration_url"
                ),
                "is_enterprise_install": is_enterprise_install,
                "token_type": oauth_response.get("token_type"),
            }

            logger.info(f"Slack OAuth callback, activating user credentials for user_id: {user.id} with oauth state token: {state}")

            user_creds = user_service.activate_user_credentials(
                user,
                state,
                ServiceProviders.SLACK.value,
                installation_credentials["user_id"],
                json.dumps(installation_credentials),
            )

            logger.info(f"Slack OAuth callback, user credentials activated for user_id: {user.id} with service_user_id: {user_creds.service_user_id} in workspace: {user_creds.service_workspace_name}")
            return "Success! Bot installed."

        else:
            return make_response(f"Try the installation again (the state value is already expired)", 400)

    error = request.args["error"] if "error" in request.args else ""
    return make_response(f"Something is wrong with the installation (error: {html.escape(error)})", 400)


# Slack event handling starts here
@slack_bp.route("/slack/events", methods=["POST"])
def slack_events():
    # payload = request.json
    logger.info(
        f"Slack Events Route Received Slack Event for user: {session.get('user_id')}"
    )

    return handler.handle(request)


@slack_app.event("message")
def process_message_events(event, say):
    from app import get_db_session_maker
    # put the message onto the celery queue
    logger.info(f"Processing slack event: {event}")
    from bespokebots.services.user_service import UserService

    try:
        Session = get_db_session_maker()
        db_sesh = Session()
        say("Got your message! Reading it now...")
        user = UserService.lookup_by_service_user_id(ServiceProviders.SLACK.value,event["user"],db_sesh)
        Session.remove()
        logger.info(f"Processing slack message from user: {user.id}")

        process_slack_message.delay(user.id, event["channel"], event["text"])

    except Exception as e:
        logger.exception(f"Error processing slack message: %s", e)
        say(
            f"Sorry, I couldn't process your message. The following error occurred: {str(e)}"
        )


@slack_bp.route("/slack/interactive", methods=["POST"])
def slack_interactive():
    return handler.handle(request)


@slack_app.event("app_mention")
def process_mention_events(event, say):
    say("Hello there!")


@slack_app.action("create_event")
def handle_create_event(ack: Ack, action, client, response_url):
    # Don't forget to acknowledge the action within 3 seconds
    ack()

    values = action["view"]["state"]["values"]
    event_details = {
        "start_time": values["start_time_block"]["start_time_action"][
            "selected_option"
        ]["value"],
        "end_time": values["end_time_block"]["end_time_action"]["selected_option"][
            "value"
        ],
        "title": values["title_block"]["title_action"]["value"],
        "description": values["description_block"]["description_action"]["value"],
    }

    # Create the event using Google Calendar Client
    calendar_client = create_authenticated_client()
    calendar_client.create_event(event_details)

    # Notify the user about the creation of the event
    client.chat_postMessage(
        channel=response_url, text=f"Event '{event_details['title']}' has been created!"
    )


@slack_app.view_submission("event_modal")
def handle_view_submission(ack: Ack, view, client, trigger_id):
    # Don't forget to acknowledge the view_submission event within 3 seconds
    ack()

    selected_slot = view["state"]["values"]["slot_selection_block"][
        "slot_selection_action"
    ]["selected_option"]["value"]

    # Prepare the modal to create event
    view = generate_event_creation_modal(selected_slot)
    client.views_open(trigger_id=trigger_id, view=view)
