
class GoogleCalendarInstance:
    def __init__(self, cal_id, summary):
        self.id = cal_id
        self.summary = summary
    

    def to_dict(self):
        return {
            'id': self.id,
            'summary': self.summary
        }