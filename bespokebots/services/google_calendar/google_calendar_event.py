import datetime
from zoneinfo import ZoneInfo
import json



#The start and end dates are supposed to be nested objects shaped like:
# "start": 
#{
#     "date": date,
#     "dateTime": datetime,
#     "timeZone": string
#   },
#   "end": {
#     "date": date,
#     "dateTime": datetime,
#     "timeZone": string
#   },

class GoogleCalendarEvent:
    def __init__(self, timezone, start_time, end_time, summary):
        self.id = None #the id will only be set after the event is created on the calendar, set by the API
        self.htmlLink = None #the link to the event on the calendar, set by the API
        self.start = GoogleCalendarDateTime(start_time, timezone)
        self.end = GoogleCalendarDateTime(end_time, timezone)
        self.summary = summary
        self.location = None
        self.description = None
        self.color_id = None #https://developers.google.com/calendar/api/v3/reference/colors
        self.attendees = None
        self.recurrence = None
        self.reminders = None

    def location(self, location):
        self.location = location
        return self

    def description(self, description):
        self.description = description
        return self

    def to_dict(self):
        base_dict = {
            'start': self.start.to_dict(),
            'end': self.end.to_dict(),
            'summary': self.summary,
            'location': self.location,
            'description': self.description,
            'colorId': self.color_id,
            'attendees': self.attendees,
            'recurrence': self.recurrence,
            'reminders': self.reminders
        }
        return {key: value for key, value in base_dict.items() if value is not None}

    
    def build(self):
        return self.to_dict()


class GoogleCalendarDateTime:
    def __init__(self, date_time, time_zone: ZoneInfo):
        self.date_time = date_time
        self.time_zone = time_zone

    def to_dict(self):
        return {
            'dateTime': self.date_time,
            'timeZone': self.time_zone.key
        }
    

#Need helper classes for Attendees, ColorID, Recurrence, and Reminders