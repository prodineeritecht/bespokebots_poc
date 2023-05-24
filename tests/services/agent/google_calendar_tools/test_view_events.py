import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime

from bespokebots.services.agent.google_calendar_tools import GoogleCalendarBaseTool
from bespokebots.services.agent.google_calendar_tools import GoogleCalendarViewEventsTool


def test_view_events_with_specified_range():
    """Test the view events tool with a specified time range."""
    tool = GoogleCalendarViewEventsTool() # Create the tool
    events = tool.run(calendar_id='primary')
    assert len(events) > 0