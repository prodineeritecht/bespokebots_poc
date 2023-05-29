
class GoogleCalendarEntry:
    def __init__(self, title, start, end, description, summary, location, attendees, event_id=None):
        self.title = title
        self.start = start
        self.end = end
        self.description = description
        self.summary = summary
        self.location = location
        self.attendees = attendees
        self.event_id = event_id

    def __str__(self):
        return f"Event Id: {self.event_id}  \nTitle: {self.title}\nStart: {self.start}\nEnd: {self.end}\nDescription: {self.description}\nSummary: {self.summary}\nLocation: {self.location}\nAttendees: {self.attendees}"
    
    def to_dict(self):
        return {
            'event_id': self.event_id,
            'title': self.title,
            'start': self.start,
            'end': self.end,
            'description': self.description,
            'summary': self.summary,
            'location': self.location,
            'attendees': self.attendees
        }
