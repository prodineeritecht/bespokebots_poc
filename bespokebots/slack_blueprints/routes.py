from flask import Blueprint, jsonify, request
from flask import Response
import os
import logging
from slack_bolt import App, Ack
from slack_bolt.adapter.flask import SlackRequestHandler
from bespokebots.services.celery_tasks import (
    slack_app,
    process_slack_message
    )
logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)


slack_bp = Blueprint('slack', __name__)
handler = SlackRequestHandler(slack_app)

@slack_bp.route('/slack/events', methods=['POST'])
def slack_events():
    #payload = request.json
    logger.info("Slack Events Route Received Slack Event")

    # # Handle URL verification
    # if payload.get("type") == "url_verification":
    #     return Response(payload.get("challenge"))

    # Otherwise, let slack_bolt handle the event
    return handler.handle(request)

@slack_bp.route('/slack/interactive', methods=['POST'])
def slack_interactive():
    return handler.handle(request)

@slack_app.event("message")
def process_message_events(event, say):
    #put the message onto the celery queue
    logger.info(f"Processing slack event: {event}")
    say("Got your message! Reading it now...")
    process_slack_message.delay(event["user"], event["channel"], event["text"])


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