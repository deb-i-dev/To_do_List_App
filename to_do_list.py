import json
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['description'], task_dict['completed'])

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.save_tasks()

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            self.save_tasks()
        else:
            print("Invalid task number")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
        else:
            print("Invalid task number")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            tasks_dict = [task.to_dict() for task in self.tasks]
            json.dump(tasks_dict, file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    tasks_dict = json.load(file)
                    self.tasks = [Task.from_dict(task) for task in tasks_dict]
            except json.JSONDecodeError:
                print(f"Error reading {self.filename}. File might be empty or corrupt.")
                self.tasks = []
