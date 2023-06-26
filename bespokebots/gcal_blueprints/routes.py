from flask import Blueprint, jsonify, request
import logging

from bespokebots.services.google_calendar.google_calendar_client import (
    GoogleCalendarClient
)

gcal_bp = Blueprint('gcal', __name__)
# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# @gcal_bp.route('/services/calendar/connect', methods=['GET'])
# def connect_calendar():
    
#     logger.info("Received request to connect to Google Calendar")
#     calendar_client = create_authenticated_client()
#     #get the calendar list
#     calendar_list =  calendar_client.get_calendar_list()
#     if not calendar_list:
#         return "No calendars found"
#     else:
#         calendars_dict = [entry.to_dict() for entry in calendar_list]   
#         return jsonify(calendars_dict)
    
@gcal_bp.route("/services/calendar/events", methods=["GET"])
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
    logger.info("Creating authenticated Google Calendar client")
    if scopes is None:
        scopes = ['https://www.googleapis.com/auth/calendar']
    if credentials_file is None:
        credentials_file = 'credentials.json'

    # Initialize the client
    client = GoogleCalendarClient(credentials_file, scopes)
    client.authenticate()
    logger.info("Google Calendar client authenticated, returning the client")
    return client




