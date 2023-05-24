# conftest.py
import pytest
import json
import os
import datetime
from zoneinfo import ZoneInfo
from bespokebots.services.google_calendar.google_calendar_client import GoogleCalendarClient
from bespokebots.services.google_calendar.google_calendar_event import GoogleCalendarEvent


@pytest.fixture
def load_json_data():
    def _load_json_data(filename):
        with open(os.path.join('tests', 'resources', filename)) as f:
            return json.load(f)
    return _load_json_data


@pytest.fixture
def create_event():
    def _create_event(calendar_id: str, summary: str, timezone: str):
        tz = ZoneInfo(timezone)
        start_time = datetime.datetime.now(tz=tz).replace(microsecond=0).isoformat()
        end_time = (datetime.datetime.now(tz=tz).replace(microsecond=0) + datetime.timedelta(hours=1)).isoformat()
    
        credentials = '../credentials.json'
        scopes = ['https://www.googleapis.com/auth/calendar']
    
        google_calendar_client = GoogleCalendarClient(credentials, scopes)
        google_calendar_client.authenticate()

        event = GoogleCalendarEvent(tz, start_time, end_time, summary)
        event.description = "This event created by an automated test"
        response = google_calendar_client.create_event(calendar_id, event)

        return google_calendar_client, response

    return _create_event
