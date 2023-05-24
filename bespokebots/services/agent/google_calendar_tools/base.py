"""Base class for Gmail tools."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from langchain.tools.base import BaseTool
from bespokebots.services.agent.google_calendar_tools.utils import build_calendar_client


if TYPE_CHECKING:
    from googleapiclient.discovery import Resource
    from googleapiclient.discovery import build as build_resource
else:
    try:
        from googleapiclient.discovery import Resource
        from googleapiclient.discovery import build as build_resource
    except ImportError:
        pass

class GoogleCalendarBaseTool(BaseTool):
    gcal_client: GoogleCalendarClient = Field(default_factory=build_calendar_client)

    @classmethod
    def from_gcal_client(cls, gcal_client: GoogleCalendarClient) -> GoogleCalendarBaseTool:
        return cls(gcal_client=gcal_client)