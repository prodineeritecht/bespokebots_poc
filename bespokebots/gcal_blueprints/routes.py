from flask import Blueprint, jsonify, request, session, redirect, url_for
import logging
from bespokebots.models.user import User

from bespokebots.services.google_calendar.google_calendar_client import (
    GoogleCalendarClient
)

gcal_bp = Blueprint('gcal', __name__)
# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@gcal_bp.route('/services/calendar/connect', methods=['GET'])
def connect_calendar():

    logger.info("Received request to connect to Google Calendar")
    calendar_client = create_authenticated_client()
    #get the calendar list
    calendar_list =  calendar_client.get_calendar_list()
    if not calendar_list:
        return "No calendars found"
    else:
        calendars_dict = [entry.to_dict() for entry in calendar_list]   
        return jsonify(calendars_dict)
    
@gcal_bp.route("/services/oauth/calendar/connect", methods=["GET"])
def oauth_connect_calendar():
    logger.info(f"Received request to connect to Google Calendar for user {session.get('user_id')}")
    try:
        user_id = session.get('user_id')
        user = User(user_id) if user_id else None
        creds_file = f"{user_id}.json"
        calendar_client = GoogleCalendarClient(creds_file,['https://www.googleapis.com/auth/calendar'],user)
        redirect_uri = request.url_root.rstrip('/') + url_for('gcal.oauth_callback')
        auth_url = calendar_client.initiate_oauth_flow(redirect_uri, user)
        return redirect(auth_url)
    
    except Exception as e:
        logger.exception("Error connecting to Google Calendar: %s", e)
        return f"Error connecting to Google Calendar: {e}", 500

#https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=38992558726-n9en7smp0r5320gd86o623klba3jsjga.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fd9ff-198-255-250-229.ngrok-free.app%2Fservices%2Foauth%2Fcalendar%2Fcallback&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar&state=r3EJIGITeKqK389gF6W842QQdJSP9J&access_type=offline&include_granted_scopes=true&prompt=consent
#https://d9ff-198-255-250-229.ngrok-free.app/services/oauth/calendar/callback?state=r3EJIGITeKqK389gF6W842QQdJSP9J&code=4/0AZEOvhUyzUpVtJtI0kRSrGo_RCiEw47mdDYR0KId50kBDLI9scXvkY91mqbMqRvdKRSZXQ&scope=https://www.googleapis.com/auth/calendar
#'https://d9ff-198-255-250-229.ngrok-free.app/services/oauth/calendar/callback?state=KMGxZ7EWeN2tMjsStRsFatQ7faUKwI&code=4/0AZEOvhUYjjvOFQPCnh1PWcrVguSarwT4LkGM1xY5sKOloYcIjCGh5ck6dsqJF7ZlvAccYw&scope=https://www.googleapis.com/auth/calendar'
@gcal_bp.route("/services/oauth/calendar/callback", methods=["GET"])
def oauth_callback():
    logger.info("Google Calendar OAuth callback received")
    try:
        user_id = session.get('user_id')
        user = User(user_id) if user_id else None
        google_client = GoogleCalendarClient(f"users/{user_id}.json", ['https://www.googleapis.com/auth/calendar'], user)
        config = google_client.get_client_config_from_env()
        redirect_url = config['web']['redirect_uris'][0]
        google_client.authenticate_oauth(request.url, redirect_url)
        
        calendar_list =  google_client.get_calendar_list()
        if not calendar_list:
            return "No calendars found"
        else:
            calendars_dict = [entry.to_dict() for entry in calendar_list]   
            return jsonify(calendars_dict)
        
    except Exception as e:
        logger.exception("Error connecting to Google Calendar: %s", e)
        return f"Error connecting to Google Calendar: {e}", 500
    
    
@gcal_bp.route("/services/calendar/events", methods=["GET"])
def get_calendar_events():
    try:
        user_id = session.get('user_id')
        user = User(user_id) if user_id else None
        google_client = GoogleCalendarClient(f"users/{user_id}.json", ['https://www.googleapis.com/auth/calendar'], user)
        google_client.initialize_client(user_id)
        # Use the client now to perform operations on the calendar:
        events = google_client.get_calendar_events()
    
        if not events:
            return "No events found"
        else:
            event_summaries_dict = [entry.to_dict() for entry in events]
            return jsonify(event_summaries_dict)
    except Exception as e:
        logger.exception("Error getting calendar events: %s", e)
        return f"Error getting calendar events {e}", 500
    

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




