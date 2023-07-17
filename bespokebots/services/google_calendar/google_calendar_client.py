import os
from google_auth_oauthlib.flow import InstalledAppFlow, Flow 
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
from zoneinfo import ZoneInfo
from dateutil.parser import parse
import json
import pickle
import logging
from bespokebots.models.user import User
#from bespokebots.services.google_calendar.google_calendar_client import credentials_to_dict

from bespokebots.services.google_calendar.google_calendar_busy_entry import (
    GoogleCalendarBusyEntry,
)
from bespokebots.services.google_calendar.google_calendar_entry import (
    GoogleCalendarEntry,
)
from bespokebots.services.google_calendar.google_calendar_instance import (
    GoogleCalendarInstance,
)
from bespokebots.services.google_calendar.google_calendar_event import (
    GoogleCalendarEvent,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GoogleCalendarClient:
    def __init__(self, credentials_file, scopes, user: User = None):
        self.user = user
        self.credentials_file = credentials_file
        self.scopes = scopes
        self.creds = None
        self.service = None
        self.calendar_list = []
        self.environment = os.environ.get("ENVIRONMENT", "localdev")

    def authenticate(self):
        if os.path.exists("token.json"):
            self.creds = self._load_credentials()
            self._build_service()

        # If there are no (valid) credentials available, prompt the user to log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.scopes
                )
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            self._save_credentials()
            # build the service
            self._build_service()

    def _load_credentials(self):
        return self._load_from_file("token.json")

    def _save_credentials(self):
        self._save_to_file("token.json", self.creds)

    def _load_from_file(self, filename):
        with open(filename, "rb") as token:
            return pickle.load(token)

    def _save_to_file(self, filename, data):
        with open(filename, "wb") as token:
            pickle.dump(data, token)

    def _build_service(self):
        self.service = build("calendar", "v3", credentials=self.creds)

    def get_service(self):
        if not self.service:
            self._build_service()
        return self.service

    #None of the previous methods depend on the User object.  The following auth methods do.
    #Functions for supporting the full Oauth2 flow
    # New method to initiate OAuth flow
    def initiate_oauth_flow(self, redirect_uri, user):
        
        self.flow = Flow.from_client_config(
            self.get_client_config_from_env(), 
            scopes=self.scopes,
            redirect_uri=redirect_uri
        )
        authorization_url, state = self.flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent'
        )
        user.save_state(state)
        return authorization_url
    
    # New method to authenticate using OAuth flow5
    def authenticate_oauth(self, authorization_response, redirect_uri):
        state = self.user.state
        flow = Flow.from_client_config(
            self.get_client_config_from_env(),
            scopes=self.scopes,
            state=state,
            redirect_uri=redirect_uri
        )
        flow.fetch_token(authorization_response=authorization_response)
        self.user.credentials = self.credentials_to_dict(flow.credentials)
        self.user._save()
        self.creds = Credentials.from_authorized_user_info(self.user.credentials)
        self._build_service()

     
    def initialize_client(self, user_id):
        self.user = User.lookup_by_user_id(user_id)
        self.creds = Credentials.from_authorized_user_info(self.user.credentials)
        self._build_service()
        
    
    def get_client_config_from_env(self):
        logger.info("Getting client config from environment. env[REDIRECT_URIS] = %s", os.getenv("REDIRECT_URIS"))
        web_info = {
            "client_id": os.getenv("CLIENT_ID"),
            "project_id": os.getenv("PROJECT_ID"),
            "auth_uri": os.getenv("AUTH_URI"),
            "token_uri": os.getenv("TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            "redirect_uris": os.getenv("REDIRECT_URIS").split(','),  # assuming comma-separated values
        }
        return {"web": web_info}
    
    def credentials_to_dict(self, credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}
            
    
    # Functions related to working with the GCal API
    def get_calendar_list(self) -> list[GoogleCalendarInstance]:
        """Retrieve a list of calendars"""
        self.calendar_list = self.service.calendarList().list().execute()
        # json_list = json.dumps(self.calendar_list, indent=4)
        # print(json_list)

        calendars = []
        for calendar in self.calendar_list["items"]:
            new_calendar = GoogleCalendarInstance(calendar["id"], calendar["summary"])
            calendars.append(new_calendar)

        return calendars

    def get_calendar_events(
        self, calendar_id=None, start_date=None, end_date=None
    ) -> list[GoogleCalendarEntry]:
        """Retrieve events from a calendar between two dates"""
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

        _calendar, _start_date, _end_date = self._validate_calendar_inputs(
            calendar_id, start_date, end_date, now
        )

        events_result = (
            self.service.events()
            .list(
                calendarId=_calendar,
                timeMin=_start_date,
                timeMax=_end_date,
                maxResults=100,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        # json_events = json.dumps(events_result, indent=4)
        # print(json_events)
        events = events_result.get("items", [])

        if not events:
            return None

        # Prep the party list, broh
        event_summaries = []
        for event in events:
            # Look at all that juicy event data. Let's pull it out.
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            attendees = [
                att["email"] for att in event.get("attendees", [])
            ]  # Watch out for events with no attendees

            # Alright, let's make a new guest for our party
            new_entry = GoogleCalendarEntry(
                event_id=event["id"],
                title=event["summary"],
                start=start,
                end=end,
                description=event.get("description", ""),
                summary=event.get("summary", ""),
                location=event.get("location", ""),
                attendees=attendees,
            )

            # And add 'em to the list!
            event_summaries.append(new_entry)

        return event_summaries

    def get_event(self, calendar_id, event_id):
        """Retrieve a single event from a calendar"""
        event = (
            self.service.events()
            .get(calendarId=calendar_id, eventId=event_id)
            .execute()
        )
        return event

    def get_busy_time(
        self, calendar_id=None, start_date=None, end_date=None
    ) -> list[GoogleCalendarBusyEntry]:
        """Retrieve busy time from a calendar between two dates"""
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

        _calendar, _start_date, _end_date = self._validate_calendar_inputs(
            calendar_id, start_date, end_date, now
        )

        query_body = {
            "timeMin": _start_date,
            "timeMax": _end_date,
            "timeZone": "America/New_York",
            "items": [{"id": _calendar}],
        }

        events_result = self.service.freebusy().query(body=query_body).execute()

        json_events = json.dumps(events_result, indent=4)
        print(json_events)

        # Freebusy events will be objects with the following structure:
        # {
        #    start: datetime,
        #    end: datetime
        # }
        busy_events = (
            events_result.get("calendars", {calendar_id})
            .get(_calendar, {})
            .get("busy", [])
        )
        busy_entries = []
        for event in busy_events:
            busy_entries.append(
                GoogleCalendarBusyEntry(
                    parse(event["start"]), parse(event["end"]), calendar_id
                )
            )

        return busy_entries

    def create_event(self, calendar_id, event: GoogleCalendarEvent):
        """Creates a new event on a user's calendar"""

        event_body = (
            event.build()
        )  # Serializes the GoogleCalendarEvent object into a JSON object
        response = (
            self.service.events()
            .insert(calendarId=calendar_id, body=event_body)
            .execute()
        )
        return response

    def delete_event(self, calendar_id, event_id):
        """Deletes an event from a user's calendar"""
        response = (
            self.service.events()
            .delete(calendarId=calendar_id, eventId=event_id)
            .execute()
        )
        return response

    def update_event(self, calendar_id, event):
        """Updates an event on a user's calendar"""
        event_id = event.get("id")
        response = (
            self.service.events()
            .update(calendarId=calendar_id, eventId=event_id, body=event)
            .execute()
        )
        return response

    def _validate_calendar_inputs(
        self, calendar_id, start_date, end_date, now, tz=ZoneInfo("America/New_York")
    ):
        if not calendar_id:
            # just use the primary calendar
            _calendar = "primary"
        else:
            _calendar = calendar_id

        # If the start date wasn't provided, use today as the start date
        if not start_date:
            _start_date = now
        else:
            _start_date = start_date

        # If the end date wasn't provided, use a week from today as the end date
        if not end_date:
            _end_date = (
                datetime.datetime.now(tz=tz) + datetime.timedelta(days=7)
            ).isoformat()
        else:
            _end_date = end_date
        return _calendar, _start_date, _end_date
