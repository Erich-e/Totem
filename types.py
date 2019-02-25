"""
Task datatype
"""

from datetime import datetime

class Task():
    def __init__(self, name="", description="", priority=0, due_date=None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.created_at = datetime.now()
        self.priority = priority
        self.tags = []
        self.complete = False

    def isComplete(self):
        return self.complete

class Event(Task):
    def __init__(self, name, description="", priority=0, due_date=None):
        Task.__init__(name, description, priority, due_date)

    def isComplete(self):
        return datetime.now() > self.due_date