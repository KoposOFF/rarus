class Task:
    def __init__(self, title, priority):
        self.id = None  # ID будет назначен при добавлении в хранилище
        self.title = title
        self.priority = priority

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'priority': self.priority
        }
