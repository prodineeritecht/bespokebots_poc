from typing import List, Optional, Type

from pydantic import BaseModel, Field
from zoneinfo import ZoneInfo

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from bespokebots.dao.database import db
from bespokebots.services.agent.google_calendar_tools.base import GoogleCalendarBaseTool
from bespokebots.services.google_calendar import (
    GoogleCalendarEvent
)

class CreateEventSchema(BaseModel):
    """Schema for the CreateEventTool."""

    calendar_id: str = Field(
        ...,
        title="Calendar ID",
        description="The ID of the calendar to create the event on."
    )

    user_id: str = Field(
        ...,
        title="User ID",
        description="The user's ID, necessary for ensuring the calendar client is able to authenticate to Google."
    )

    summary: str = Field(
        ...,
        title="Summary",
        description="The title of the event."
    )
    timezone: str = Field(
        ...,
        title="Timezone",
        description="The timezone to create the event in."
    )
    start_time: str = Field(
        None,
        title="Start Time",
        description="The start date and time of the event. In ISO 8601 format with timezone offset."
    )
    end_time: str = Field(
        None,
        title="End Time",
        description="The end date and time of the event. In ISO 8601 format with timezone offset."
    )
    description: Optional[str] = Field(
        None,
        title="Description",
        description="The description of the event."
    )
    location: Optional[str] = Field(
        None,
        title="Location",
        description="The location of the event."
    )
    attendees: Optional[List[str]] = Field(
        None,
        title="Attendees",
        description="The attendees of the event."
    )

class GoogleCalendarCreateEventTool(GoogleCalendarBaseTool):
    name: str = "create_calendar_event"
    description: str = """Use this tool to create an event on a human's Google Calendar. Right now, this tool can only create one event
    at a time. The tool will return the event that was created. The default timezone is America/New_York. 
    """
    args_schema: Type[CreateEventSchema] = CreateEventSchema

    def _run(
            self,
            calendar_id: str,
            user_id: str,
            summary: str,
            timezone: str,
            start_time: str,
            end_time: str,
            description: Optional[str] = None,
            location: Optional[str] = None,
            attendees: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> dict:
        try:
            #ensure the gcal_client has been authenticated
            sesh = db.session
            self.gcal_client.initialize_client(user_id)

            tz = ZoneInfo(timezone)
            event_body =  GoogleCalendarEvent(tz, start_time, end_time, summary)  
            event_body.location = location
            event_body.description = description
            event_body.attendees = attendees

            event = self.gcal_client.create_event(
                calendar_id, event_body
            )
            return event
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        


    async def _arun(
            self,
            calendar_id: str,
            summary: str,
            timezone: str,
            start_time: str,
            end_time: str,
            description: Optional[str] = None,
            location: Optional[str] = None,
            attendees: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> dict:
        raise NotImplementedError(f"The tool {self.name} does not support async yet.")