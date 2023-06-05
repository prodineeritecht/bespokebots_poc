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
        description="The start time of the time range to view events from. In ISO 8601 format with a timezone offest or Z for UTC.",
    )
    time_max: Optional[str] = Field(
        None,
        title="Time Max",
        description="The end time of the time range to view events from. In ISO 8601 format with a timezone offest or Z for UTC.",
    )


class GoogleCalendarViewEventsTool(GoogleCalendarBaseTool):
    """Tool for viewing events in Google Calendar."""

    name: str = "view_calendar_events"
    description: str = """Use this tool to help you answer questions a human may have about their schedule or when important events are happening. 
    Think of this as the your calendar search tool. If the human doesn't specify a time range, the tool will default to looking one week in advance. 
    Unles otherwise specified, use America/New_York as the user's timezone . Additionally, all dates need to be in ISO 8601 format with a timezone offset or Z for UTC"""

    args_schema: Type[ViewEventsSchema] = ViewEventsSchema

    def _run(
        self,
        calendar_id: str,
        time_min: Optional[str] = None,
        time_max: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> dict:
        """View events in Google Calendar."""
        try:
            #ensure the gcal_client has been authenticated
            self.gcal_client.authenticate()

            gcal_events = self.gcal_client.get_calendar_events(
                calendar_id, time_min, time_max
            )
        
            events = [event.to_dict() for event in gcal_events]
            return events
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    async def _arun(self, calendar_id: str, time_min: str, time_max: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> dict:
        raise NotImplementedError(f"The tool {self.name} does not support async yet.")
