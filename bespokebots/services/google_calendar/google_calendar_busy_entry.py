
import datetime

class GoogleCalendarBusyEntry:
    def __init__(self,start: datetime, end: datetime, calendar_id: str):
        if not isinstance(start, datetime.datetime):
            raise ValueError("start must be a datetime instance")
        if not isinstance(end, datetime.datetime):
            raise ValueError("end must be a datetime instance")
        if not isinstance(calendar_id, str):
            raise ValueError("calendar_id must be a string")
        self.start = start
        self.end = end
        self.calendar_id = calendar_id

    
    def to_dict(self):
        return {
            'start': self.start,
            'end': self.end,
            'calendar_id': self.calendar_id
        }