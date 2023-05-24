
class GoogleCalendarEntry:
    def __init__(self, title, start, end, description, summary, location, attendees):
        self.title = title
        self.start = start
        self.end = end
        self.description = description
        self.summary = summary
        self.location = location
        self.attendees = attendees

    def __str__(self):
        return f"Title: {self.title}\nStart: {self.start}\nEnd: {self.end}\nDescription: {self.description}\nSummary: {self.summary}\nLocation: {self.location}\nAttendees: {self.attendees}"
    
    def to_dict(self):
        return {
            'title': self.title,
            'start': self.start,
            'end': self.end,
            'description': self.description,
            'summary': self.summary,
            'location': self.location,
            'attendees': self.attendees
        }
