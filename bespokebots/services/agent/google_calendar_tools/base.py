"""Base class for Gmail tools."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from langchain.tools.base import BaseTool
from bespokebots.services.google_calendar import (
    GoogleCalendarClient
)

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource
from googleapiclient.discovery import build as build_resource
from bespokebots.services.agent.google_calendar_tools.utils import build_calendar_client


class GoogleCalendarBaseTool(BaseTool):
    gcal_client: GoogleCalendarClient = Field(default_factory=build_calendar_client)

    @classmethod
    def from_gcal_client(
        cls, gcal_client: GoogleCalendarClient
    ) -> GoogleCalendarBaseTool:
        return cls(gcal_client=gcal_client)
