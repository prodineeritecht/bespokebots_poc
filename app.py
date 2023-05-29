import os

from flask import Flask, jsonify
from slack_bolt import App, Ack
from slack_bolt.adapter.flask import SlackRequestHandler

from bespokebots.services.google_calendar.google_calendar_client import \
    GoogleCalendarClient

# Create a Flask web server from the 'app' module name
flask_app = Flask(__name__)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("BESPOKE_BOTS_SLACK_BOT_TOKEN"),
    signing_secret= os.environ.get("BESPOKE_BOTS_SLACK_SIGNING_SECRET")
)

@app.message("hello")
def message_hello(message, say):
    say("Hello there!")

handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

@flask_app.route("/slack/interactive", methods=["POST"])
def slack_interactive():
    return handler.handle(request)

@app.action("create_event")
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

@app.view_submission("event_modal")
def handle_view_submission(ack: Ack, view, client, trigger_id):
    # Don't forget to acknowledge the view_submission event within 3 seconds
    ack()
    
    selected_slot = view["state"]["values"]["slot_selection_block"]["slot_selection_action"]["selected_option"]["value"]
    
    # Prepare the modal to create event
    view = generate_event_creation_modal(selected_slot)
    client.views_open(trigger_id=trigger_id, view=view)

@flask_app.route("/services/calendar/connect", methods=["GET"])
def connect_calendar():
    
    calendar_client = create_authenticated_client()
    #get the calendar list
    calendar_list =  calendar_client.get_calendar_list()
    if not calendar_list:
        return "No calendars found"
    else:
        calendars_dict = [entry.to_dict() for entry in calendar_list]   
        return jsonify(calendars_dict)



@flask_app.route("/services/calendar/events", methods=["GET"])
def get_calendar_events():
    calendar_client = create_authenticated_client()
    events = calendar_client.get_calendar_events() 
    if not events:
        return "No events found"
    else:
        event_summaries_dict = [entry.to_dict() for entry in events]
        return jsonify(event_summaries_dict)



#helper functions
def create_authenticated_client(scopes=None, credentials_file=None):
    """Creates an authenticated Google Calendar client."""
    # If scopes and credentials_file parameters are not provided, use defaults
    if scopes is None:
        scopes = ['https://www.googleapis.com/auth/calendar']
    if credentials_file is None:
        credentials_file = 'credentials.json'

    # Initialize the client
    client = GoogleCalendarClient(credentials_file, scopes)
    client.authenticate()
    return client


if __name__ == "__main__":
    flask_app.run(port=3000)
