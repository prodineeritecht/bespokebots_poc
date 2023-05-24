import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from bespokebots.services.google_calendar.google_calendar_entry import GoogleCalendarEntry
from bespokebots.services.google_calendar.google_calendar_instance import GoogleCalendarInstance   
from bespokebots.services.google_calendar.google_calendar_client import GoogleCalendarClient
from bespokebots.services.google_calendar.google_calendar_busy_entry import GoogleCalendarBusyEntry
from bespokebots.services.google_calendar.google_calendar_event import GoogleCalendarEvent
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

    





# def test_get_busy_time_for_a_given_timeframe():
#     #Given that an LLM can interpret "free time blocks" from a set of busy times
#     # over some time period, I don't think I need this functionality.  Going to just disable this test
#     # for now.  I'll revisit this later.
#     #credentials = Mock(valid=True)
#     credentials = '../../../credentials.json'
#     scopes = ['https://www.googleapis.com/auth/calendar']
    
#     google_calendar_client = GoogleCalendarClient(credentials, scopes)
#     google_calendar_client.authenticate()

#     free_time_list = google_calendar_client.get_free_time('primary', '2023-05-19T00:00:00Z', '2023-05-29T00:00:00Z')

#     assert 0 < len(free_time_list)

# def test_free_time_calcualator():
#     # Define the total time period we're considering
#     start_time = datetime.datetime(2023, 5, 18, 0, 0)
#     end_time = start_time + datetime.timedelta(days=7)


#     # Define some busy intervals for testing
#     busy_intervals = [
#         {"start": start_time + datetime.timedelta(hours=9), "end": start_time + datetime.timedelta(hours=10)},
#         {"start": start_time + datetime.timedelta(days=1, hours=12), "end": start_time + datetime.timedelta(days=1, hours=13)},
#         {"start": start_time + datetime.timedelta(days=2, hours=15), "end": start_time + datetime.timedelta(days=2, hours=16)},
#         {"start": start_time + datetime.timedelta(days=4, hours=9), "end": start_time + datetime.timedelta(days=4, hours=12)},
#         {"start": start_time + datetime.timedelta(days=5, hours=14), "end": start_time + datetime.timedelta(days=5, hours=18)},
#     ]

#     credentials = Mock(valid=True)
#     scopes = ['https://www.googleapis.com/auth/calendar']
#     google_calendar_client = GoogleCalendarClient(credentials, scopes)

#     freetime_intervals = google_calendar_client.free_time_calculator(start_time, end_time, busy_intervals, "primary")
#     assert 6 == len(freetime_intervals)
#     # Expected freetime intervals:
#     # From May 18, 2023 00:00 (start_time) to May 18, 2023 09:00 (beginning of the first busy interval)
#     # From May 18, 2023 10:00 (end of the first busy interval) to May 19, 2023 12:00 (beginning of the second busy interval)
#     # From May 19, 2023 13:00 (end of the second busy interval) to May 20, 2023 15:00 (beginning of the third busy interval)
#     # From May 20, 2023 16:00 (end of the third busy interval) to May 22, 2023 09:00 (beginning of the fourth busy interval)
#     # From May 22, 2023 12:00 (end of the fourth busy interval) to May 23, 2023 14:00 (beginning of the fifth busy interval)
#     # From May 23, 2023 18:00 (end of the fifth busy interval) to May 25, 2023 00:00 (end_time)
    
#     assert (start_time, start_time + datetime.timedelta(hours=9)) == (freetime_intervals[0].start, freetime_intervals[0].end)
#     assert (start_time + datetime.timedelta(hours=10), start_time + datetime.timedelta(days=1, hours=12)) == (freetime_intervals[1].start, freetime_intervals[1].end)
#     assert (start_time + datetime.timedelta(days=1, hours=13), start_time + datetime.timedelta(days=2, hours=15)) == (freetime_intervals[2].start, freetime_intervals[2].end)
#     assert (start_time + datetime.timedelta(days=2, hours=16), start_time + datetime.timedelta(days=4, hours=9)) == (freetime_intervals[3].start, freetime_intervals[3].end)
#     assert (start_time + datetime.timedelta(days=4, hours=12), start_time + datetime.timedelta(days=5, hours=14)) == (freetime_intervals[4].start, freetime_intervals[4].end)
#     assert (start_time + datetime.timedelta(days=5, hours=18), end_time) == (freetime_intervals[5].start, freetime_intervals[5].end)    


