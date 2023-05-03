from .database import database


class Task:
    self.name = "Task"
    self.description = "This is a task"
    self.date_added = "01.01.1900 00:00:00"
    self.date_due = "01.01.2000 00:00:00"
    self.completed = False

    def __init__(self, name: str = "Task", description: str = "This is a task", date_added: str = "01.01.1900 00:00:00", date_due: str = "01.01.2000 00:00:00", completed: bool = False):
        self.name = name
        self.description = description
        self.date_added = date_added
        self.date_due = date_due
        # Request save to database

    def complete_task(self):
        self.completed = True
        # Request change in database

    def delete_task(self, task_id: int):
        database.delete_task(task_id)
        # if failed, show that in the cli


def get_all_tasks():
    return database.get_all()


def run():
    id = 0
    if get_all_tasks() is None:
        id = database.Database.data['tasks'][-1]['id']
    id += 12  # because my lsp deletes id
