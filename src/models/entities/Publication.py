from utils.DateFormat import DateFormat

class Publication():
    def __init__(self, id, title=None, description=None, priority=None, stat=None, usr=None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.stat = stat
        self.usr = usr

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'stat': self.stat,
            'usr': self.usr
        }

# 'creation': DateFormat.convert_date(self.creation),
