"""Utility functions for Google Calendar tools."""
import logging
import os
from typing import TYPE_CHECKING, List, Optional, Tuple
from bespokebots.services.google_calendar import (
    GoogleCalendarEntry,
    GoogleCalendarInstance,
    GoogleCalendarClient,
    GoogleCalendarBusyEntry,
    GoogleCalendarEvent
)
from bespokebots.dao.database import db
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build as build_resource

logger = logging.getLogger(__name__)


def import_google_auth_oauthlib_flow() -> InstalledAppFlow:
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        raise ValueError(
            "You need to install google_auth_oauthlib to use this toolkit. "
            "Try running pip install --upgrade google-auth-oauthlib"
        )
    return InstalledAppFlow

def import_googleapiclient_discovery() -> build_resource:
    try:
        from googleapiclient.discovery import build
    except ImportError:
        raise ValueError(
            "You need to install googleapiclient to use this toolkit. "
            "Try running pip install --upgrade google-api-python-client"
        )
    return build

def import_google_auth() -> Tuple[Credentials, Request]:
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials

    except ImportError:
        raise ValueError(
            "You need to install google-auth to use this toolkit. "
            "Try running pip install --upgrade google-auth"
        )
    return Credentials, Request

def import_google_auth_credentials() -> Credentials:
    try:
        from google.oauth2.credentials import Credentials
    except ImportError:
        raise ValueError(
            "You need to install google-auth to use this toolkit. "
            "Try running pip install --upgrade google-auth"
        )
    return Credentials

def import_googleapiclient_resource_builder() -> build_resource:
    try:
        from googleapiclient.discovery import build
    except ImportError:
        raise ValueError(
            "You need to install googleapiclient to use this toolkit. "
            "Try running pip install --upgrade google-api-python-client"
        )
    return build

DEFAULT_SCOPES = ['https://www.googleapis.com/auth/calendar']
DEFAULT_CREDS_TOKEN_FILE = "../../../../token.json"
DEFAULT_CLIENT_SECRETS_FILE = "../../../../credentials.json"


def build_calendar_and_feedback_clients(credentials: Optional[Credentials] = None,
                          scopes: Optional[List[str]] = None) -> GoogleCalendarClient:
    """Build a Google Calendar client."""

#TODO: Now that we have the full OAuth flow working, relying on the InstalledAppFlow is no longer necessary. 
# The tools should operate under the assumption that the user has already authenticated with Google and 
# has valid credentials stored in the db. In this method, the code should probably focus on validating that
# the credentials are still active and refreshing them if necessary.
    # Import the necessary modules
    InstalledAppFlow = import_google_auth_oauthlib_flow()
    Credentials, Request = import_google_auth()
    from bespokebots.services.user_service import UserService
    credentials = credentials or DEFAULT_CLIENT_SECRETS_FILE
    scopes = scopes or DEFAULT_SCOPES
    user_service = UserService(db.session)
    client = GoogleCalendarClient(credentials, scopes, user_service=user_service)
    return client
