# conftest.py
import datetime
import json
import os
from zoneinfo import ZoneInfo
from typing import List, Optional, Type

import pytest

from bespokebots.services.google_calendar import (
    GoogleCalendarClient,
    GoogleCalendarEvent,
)


@pytest.fixture
def load_json_data():
    def _load_json_data(filename):
        with open(os.path.join("tests", "resources", filename)) as f:
            return json.load(f)

    return _load_json_data


@pytest.fixture
def create_future_event():
    def _create_future_event(
        calendar_id: str,
        summary: str,
        timezone: str,
        days_from_now: int,
        hours_long: int,
    ):
        """Create a future event on the calendar specified by the calendar_id.  The event will be
        days_from_now days from now and will be hours_long hours long.

        Args:
            calendar_id (str): The calendar id to create the event on
            summary (str): The title of the event
            timezone (str): The timezone to create the event in
            days_from_now (int): The number of days from now to create the event
            hours_long (int): The number of hours long the event is

        Returns:
            google_calendar_client (GoogleCalendarClient): The google calendar client
            response (dict): The response from the google calendar api
        """
        return create_calendar_event(calendar_id, summary, timezone, days_from_now, hours_long)

    return _create_future_event


@pytest.fixture
def create_event():
    def _create_event(
        calendar_id: str,
        summary: str,
        timezone: str
    ):
        return create_calendar_event(calendar_id, summary, timezone, 0, 1)

    return _create_event



def create_calendar_event(
    calendar_id: str,
    summary: str,
    timezone: str,
    days_from_now: Optional[int] = None,
    hours_long: Optional[int] = None,
):
    """Event creation helper function.  Assumes the event begins and ends on the same day.
    If the 'hours_long' parameter is not provided, the event will be 1 hour long.

    Args:   
        calendar_id (str): The calendar id to create the event on
        summary (str): The title of the event
        timezone (str): The timezone to create the event in
        days_from_now (int): The number of days from now to create the event
        hours_long (int): The number of hours long the event is

    Returns:
        google_calendar_client (GoogleCalendarClient): The google calendar client
        response (dict): The response from the google calendar api
    """
    tz = ZoneInfo(timezone)
    now = datetime.datetime.now(tz=tz).replace(microsecond=0)
    _hours_long = 1 or hours_long
    start_time = (now + datetime.timedelta(days=days_from_now)).isoformat()
    end_time = (
        now + datetime.timedelta(days=days_from_now, hours=_hours_long)
    ).isoformat()

    credentials = "../credentials.json"
    scopes = ["https://www.googleapis.com/auth/calendar"]

    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.authenticate()

    event = GoogleCalendarEvent(tz, start_time, end_time, summary)
    event.description = "This event created by an automated test"
    response = google_calendar_client.create_event(calendar_id, event)

    return google_calendar_client, response
