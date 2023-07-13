import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from bespokebots.services.google_calendar import (
    GoogleCalendarClient,
    GoogleCalendarEvent
)

from zoneinfo import ZoneInfo

#These tests are not very good, but, they serve as as starting point!

@patch('googleapiclient.discovery.Resource')
def test_get_calendar_list(mock_resource, load_json_data ):
    credentials = Mock(valid=True)
    scopes = ['https://www.googleapis.com/auth/calendar']
    
    mock_resource.calendarList().list().execute.return_value = load_json_data('calendar_list_4_items.json')

    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.service = mock_resource

    calendar_list = google_calendar_client.get_calendar_list()
    assert 4 == len(calendar_list)

@patch('googleapiclient.discovery.Resource')
def test_get_events_for_a_given_timeframe(mock_resource, load_json_data ):
    credentials = Mock(valid=True)
    scopes = ['https://www.googleapis.com/auth/calendar']
    mock_resource.events().list().execute.return_value = load_json_data('calendar_events.json')

    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.service = mock_resource

    calendar_events = google_calendar_client.get_calendar_events('primary', '2023-05-19T00:00:00Z', '2023-05-29T00:00:00Z')
    assert 9 == len(calendar_events)

def test_get_busy_time_for_a_given_timeframe():
    #Given that an LLM can interpret "free time blocks" from a set of busy times
    # over some time period, I don't think I need this functionality.  Going to just disable this test
    # for now.  I'll revisit this later.
    #credentials = Mock(valid=True)
    credentials = '../../../credentials.json'
    scopes = ['https://www.googleapis.com/auth/calendar']
    
    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.authenticate()

    busy_time_list = google_calendar_client.get_busy_time('primary', '2023-05-19T00:00:00Z', '2023-05-29T00:00:00Z')

    assert 0 < len(busy_time_list)

def test_add_basic_event():
    """The basic event just has the start and end times as well as a summary or title"""
    # Test here with google_calendar_client
    new_york_tz = ZoneInfo('America/New_York')
    start_time = datetime.datetime.now(tz=new_york_tz ).replace(microsecond=0).isoformat()
    end_time = (datetime.datetime.now(tz=new_york_tz).replace(microsecond=0) + datetime.timedelta(hours=1)).isoformat()
    
    credentials = '../../../credentials.json'
    scopes = ['https://www.googleapis.com/auth/calendar']
    
    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.authenticate()

    event = GoogleCalendarEvent(new_york_tz, start_time, end_time, "Test Event")
    event.description = "This event created by an automated test"
    response = google_calendar_client.create_event("primary", event)
    #Go ahead and delete the event before the assertions, to keep the calendar clean
    google_calendar_client.delete_event("primary", response.get('id'))

    assert response is not None
    assert(response.get('start').get('dateTime') == start_time)
    assert(response.get('end').get('dateTime') == end_time)


def test_delete_event(create_event):
    #create an event to be deleted.  
    
    google_calendar_client, response = create_event("primary", "Delete Me!", 'America/New_York')
    eventId = response.get('id')
    assert eventId is not None

    assert (google_calendar_client.delete_event("primary", eventId) is '')
    
def test_get_an_event(create_event):
    #create an event to be deleted.  
    
    google_calendar_client, response = create_event("primary", "Find Me!", 'America/New_York')
    eventId = response.get('id')
    assert eventId is not None

    found = google_calendar_client.get_event("primary", eventId)
    google_calendar_client.delete_event("primary", eventId)
    assert found is not None
    assert found.get('id') == eventId


def test_update_event(create_event):
    google_calendar_client, response = create_event("primary", "Update Me!", 'America/New_York')

    #In order to update an event w/o deleting most of it, 
    #retrieve the event first, the update the property to be updated
    #then use the update service to upadte the full event

    eventId = response.get('id')
    response['location'] = "New Location"

    updated_event = google_calendar_client.update_event("primary",response)
    assert updated_event is not None
    assert updated_event.get('location') == "New Location"

    
def test_start_full_oauth_flow():
    credentials = '../../../credentials.json'
    scopes = ['https://www.googleapis.com/auth/calendar']
    
    google_calendar_client = GoogleCalendarClient(credentials, scopes)
    google_calendar_client.authenticate()
    assert google_calendar_client is not None
    assert google_calendar_client.service is not None
    assert google_calendar_client.credentials is not None
    assert google_calendar_client.credentials.valid is True