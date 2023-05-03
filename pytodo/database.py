import json


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.filename, 'r', 1, 'UTF-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'tasks': []}
        return data

    def _save_data(self):
        with open(self.filename, 'w', 1, 'UTF-8') as f:
            json.dump(self.data, f)

    def add_task(self, task):
        self.data['tasks'].append(task)
        self._save_data()

    def delete_task(self, task_id):
        for task in self.data['tasks']:
            if task['id'] == task_id:
                self.data['tasks'].remove(task)
                self._save_data()
                return True
        return False

    def get_all(self):
        return self.data['tasks']
