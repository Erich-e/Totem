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
