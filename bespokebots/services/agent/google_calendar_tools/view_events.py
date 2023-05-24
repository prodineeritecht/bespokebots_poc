
from typing import List, Optional, Type

from pydantic import BaseModel, Field

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from bespokebots.services.agent.google_calendar_tools.base import GoogleCalendarBaseTool

class ViewEventsSchema(BaseModel):
    """Schema for the ViewEventsTool."""

    calendar_id: str = Field(
        ...,
        title="Calendar ID",
        description="The ID of the calendar to view events from.",
    )
    time_min: Optional[str] = Field(
        None,
        title="Time Min",
        description="The start time of the time range to view events from.",
    )
    time_max: Optional[str] = Field(
        None,
        title="Time Max",
        description="The end time of the time range to view events from.",
    )

class GoogleCalendarViewEventsTool(GoogleCalendarBaseTool):
    """Tool for viewing events in Google Calendar."""

    name: str = "view_calendar_events"
    description: str = (
        "Use this tool to fetch events from a human's Google Calendar over a specified time range. If the human didn't provide a time frame, the tool will default to the next 7 days of events."
    )
    args_schema: Type[ViewEventsSchema] = ViewEventsSchema


    def _run(self, 
             calendar_id: str, 
             time_min: Optional[str] = None, 
             time_max: Optional[str] = None,
             run_manager: Optional[CallbackManagerForToolRun] = None) -> dict:
        """View events in Google Calendar."""
        try:
            gcal_events = self.gcal_client.get_calendar_events(calendar_id, time_min, time_max)
            events = [event.to_dict() for event in gcal_events]
            return events
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
    
    
    async def _arun(self, calendar_id: str, time_min: str, time_max: str) -> dict:
        raise NotImplementedError(f"The tool {self.name} does not support async yet.")