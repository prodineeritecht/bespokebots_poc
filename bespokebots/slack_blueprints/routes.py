from flask import Blueprint, jsonify, request, session, redirect, url_for
from flask import Response
import os
import uuid
import logging
from slack_bolt import App, Ack
from slack_sdk.oauth import AuthorizeUrlGenerator
from slack_bolt.adapter.flask import SlackRequestHandler
from bespokebots.services.celery_tasks import (
    slack_app,
    process_slack_message
    )
from bespokebots.models.user import User

logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)


slack_bp = Blueprint('slack', __name__)
handler = SlackRequestHandler(slack_app)
oauth_scopes = "chat:write,app_mentions:read,channels:history,im:read"

#slack OAuth handling starts here
@slack_bp.route("/services/oauth/slack/connect", methods=["GET"])
def oauth_connect_slack():
    client_id = slack_app.client_id
    scope = oauth_scopes
    state = str(uuid.uuid4())
    redirect_uri = url_for('slack.oauth_callback_slack', _external=True)
    authorize_url = AuthorizeUrlGenerator(
        client_id=client_id, 
        scopes=scope.split(" "), 
        state=state, 
        redirect_uri=redirect_uri
    ).generate()
    
    return redirect(authorize_url)


@slack_bp.route("/services/oauth/slack/callback", methods=["GET"])
def oauth_callback_slack():
    client_id = slack_app.client_id
    client_secret = slack_app.client_secret
    redirect_uri = url_for('slack.oauth_callback_slack', _external=True)

    # flow = OAuthFlow(
    #     client_id=client_id, 
    #     client_secret=client_secret, 
    #     redirect_uri=redirect_uri
    # )
    
    code = request.args.get('code')
    state = request.args.get('state')

    # if the state does not match, this request could be a CSRF attack, abort
    if not session.get('state') == state:
        return "State does not match. Aborting."

    # response = flow.exchange_code_for_token(code)
    response = {}
    response["access_token"] = "jlaksdjfkljqadlfkjq"
    # save the token, you might want to associate it with a user
    # maybe you've stored a user_id in the session you can retrieve here
    access_token = response['access_token']
    user_id = session.get('user_id')
    user = User(user_id)
    user.set_slack_token(access_token)
    
    return "Successfully authenticated with Slack."


#Slack event handling starts here
@slack_bp.route('/slack/events', methods=['POST'])
def slack_events():
    #payload = request.json
    logger.info(f"Slack Events Route Received Slack Event for user: {session.get('user_id')}")

    return handler.handle(request)


@slack_app.event("message")
def process_message_events(event, say):
    #put the message onto the celery queue
    logger.info(f"Processing slack event: {event}")
    
    try:
        say("Got your message! Reading it now...")
        user = User.lookup_by_slack_id(event["user"])
        logger.info(f"Processing slack message from user: {user.user_id}")
        
        process_slack_message.delay(user.user_id, event["channel"], event["text"])
        
    except Exception as e:
        logger.exception(f"Error processing slack message: %s", e)
        say(f"Sorry, I couldn't process your message. The following error occurred: {str(e)}")
        
@slack_bp.route('/slack/interactive', methods=['POST'])
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
        "start_time": values["start_time_block"]["start_time_action"]["selected_option"]["value"],
        "end_time": values["end_time_block"]["end_time_action"]["selected_option"]["value"],
        "title": values["title_block"]["title_action"]["value"],
        "description": values["description_block"]["description_action"]["value"],
    }
    
    # Create the event using Google Calendar Client
    calendar_client = create_authenticated_client()
    calendar_client.create_event(event_details)
    
    # Notify the user about the creation of the event
    client.chat_postMessage(
        channel=response_url,
        text=f"Event '{event_details['title']}' has been created!"
    )

@slack_app.view_submission("event_modal")
def handle_view_submission(ack: Ack, view, client, trigger_id):
    # Don't forget to acknowledge the view_submission event within 3 seconds
    ack()
    
    selected_slot = view["state"]["values"]["slot_selection_block"]["slot_selection_action"]["selected_option"]["value"]
    
    # Prepare the modal to create event
    view = generate_event_creation_modal(selected_slot)
    client.views_open(trigger_id=trigger_id, view=view)