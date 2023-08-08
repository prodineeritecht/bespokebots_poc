import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo

from bespokebots.services.agent.google_calendar_tools import GoogleCalendarCreateEventTool

def test_create_an_event(app_fixture, _db, db_session):
    """Test the create event tool."""
    #set up the beginning and end date, the timezone must be specified.
    timezone = ZoneInfo("America/New_York")
    now = datetime.datetime.now(tz=timezone).replace(microsecond=0)
    start_time = (now + datetime.timedelta(days=1)).isoformat()
    end_time = (now + datetime.timedelta(days=1, hours=1)).isoformat()

    tool = GoogleCalendarCreateEventTool() # Create the tool
    event = tool.run({"calendar_id": "primary","user_id":"useruseruser", "summary": "Test Event", "timezone": "America/New_York", "start_time": start_time, "end_time": end_time})

    #remove the event we created
    tool.gcal_client.delete_event("primary", event["id"])
    
    assert event["summary"] == "Test Event"
    assert event["start"]["dateTime"] == start_time
    assert event["end"]["dateTime"] == end_time
