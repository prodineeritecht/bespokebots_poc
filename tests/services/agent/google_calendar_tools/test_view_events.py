import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo

from bespokebots.services.agent.google_calendar_tools import GoogleCalendarViewEventsTool


def test_view_events_with_specified_range(create_future_event):
    """Test the view events tool with a specified time range."""
    #set up the beginning and end date, the timezone must be specified.
    timezone = ZoneInfo("America/New_York")
    now = datetime.datetime.now(tz=timezone).replace(microsecond=0)
    start_time = (now + datetime.timedelta(days=7)).isoformat()
    end_time = (now + datetime.timedelta(days=14)).isoformat()
    client, future_event = create_future_event("primary", "Future Event", "America/New_York", 10, 1)  # Create a future event

    tool = GoogleCalendarViewEventsTool() # Create the tool
    events = tool.run({"calendar_id": "primary", "time_min": start_time, "time_max": end_time})
    
    #remove the event we created
    client.delete_event("primary", future_event["id"])

    assert len(events) > 0
    assert(
        any((event["summary"] == "Future Event") for event in events)
    )


def test_view_events_with_no_specified_range():
    """Test the view events tool with no specified time range."""
    tool = GoogleCalendarViewEventsTool() # Create the tool
    events = tool.run({"calendar_id": "primary"})
    assert len(events) > 0