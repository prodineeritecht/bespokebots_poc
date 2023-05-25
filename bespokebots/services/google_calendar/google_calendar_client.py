import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
from zoneinfo import ZoneInfo
from dateutil.parser import parse
import json
import pickle
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


class GoogleCalendarClient:
    def __init__(self, credentials_file, scopes):
        self.credentials_file = credentials_file
        self.scopes = scopes
        self.creds = None
        self.service = None
        self.calendar_list = []

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
