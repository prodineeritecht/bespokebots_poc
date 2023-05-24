from unittest.mock import Mock

class GoogleCalendarMock(Mock):

    def get_events(self, start_date, end_date):
        # This method simply returns a predefined list of events
        return [
            {
                'summary': 'Event 1',
                'start': {
                    'dateTime': '2023-06-01T09:00:00-07:00'
                },
                'end': {
                    'dateTime': '2023-06-01T10:00:00-07:00'
                }
            },
            # More events...
        ]

    def find_free_time(self, start_date, end_date):
        # This method simply returns a predefined list of free time slots
        return [
            {
                'start': '2023-06-01T11:00:00-07:00',
                'end': '2023-06-01T12:00:00-07:00'
            },
            # More free time slots...
        ]

    def add_event(self, details, start_time=None, end_time=None):
        # This method simply returns a success message
        return f"Event '{details}' added successfully"

    def delete_event(self, event_id):
        # This method simply returns a success message
        return f"Event '{event_id}' deleted successfully"
