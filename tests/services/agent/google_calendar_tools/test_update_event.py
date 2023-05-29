import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo

from bespokebots.services.agent.google_calendar_tools import (
    GoogleCalendarUpdateEventTool,
)


def test_update_an_event(create_future_event):
    """Test the update event tool."""

    client, future_event = create_future_event(
        "primary", "Future Event", "America/New_York", 1, 1
    )  # Create a future event

    update_fields = { "description": "This event created by Tom, the AI Assistant" }

    tool = GoogleCalendarUpdateEventTool()  # Create the tool
    event = tool.run(
        {
            "calendar_id": "primary",
            "event_id": future_event["id"],
            "update_fields": update_fields,
        }
    )

    # remove the event we created
    client.delete_event("primary", event["id"])

    assert event["summary"] == "Future Event"
    assert event["description"] == "This event created by Tom, the AI Assistant"


def test_update_an_event_with_dates_and_summary(create_future_event):
    """Test the update event tool."""
    # set up the beginning and end date, the timezone must be specified.
    timezone = ZoneInfo("America/New_York")
    now = datetime.datetime.now(tz=timezone).replace(microsecond=0)
    start_time = (now + datetime.timedelta(days=1)).isoformat()
    end_time = (now + datetime.timedelta(days=1, hours=2)).isoformat()

    client, future_event = create_future_event(
        "primary", "Future Event", "America/New_York", 1, 1
    )  # Create a future event

    update_fields = {
        "summary": "Updated Event",
        "description": "This event created by Tom, the AI Assistant"
    }

    tool = GoogleCalendarUpdateEventTool()  # Create the tool
    event = tool.run(
        {
            "calendar_id": "primary",
            "summary": future_event["summary"],
            "start_time": start_time,
            "end_time": end_time,
            "update_fields": update_fields,
        }
    )

    # remove the event we created
    client.delete_event("primary", event["id"])

    assert event["summary"] == "Updated Event"
    assert event["start"]["dateTime"] == future_event["start"]["dateTime"]
    assert event["end"]["dateTime"] == future_event["end"]["dateTime"]
    assert event["description"] == "This event created by Tom, the AI Assistant"
