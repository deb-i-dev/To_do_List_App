import tkinter as tk
from tkinter import simpledialog
from to_do_list import ToDoList
from functools import cmp_to_key

class ToDoApp:
    def __init__(self, root):
        print("Initializing ToDoApp")
        self.root = root
        self.root.title("To Do List")
        self.todo_list = ToDoList()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.sort_name_button = tk.Button(self.root, text="Sort by Name", command=self.sort_by_name)
        self.sort_name_button.pack(pady=5)

        self.sort_status_button = tk.Button(self.root, text="Sort by Status", command=self.sort_by_status)
        self.sort_status_button.pack(pady=5)

        self.filter_completed_button = tk.Button(self.root, text="Filter Completed", command=self.filter_completed)
        self.filter_completed_button.pack(pady=5)

        self.filter_incomplete_button = tk.Button(self.root, text="Filter Incomplete", command=self.filter_incomplete)
        self.filter_incomplete_button.pack(pady=5)

        self.show_all_button = tk.Button(self.root, text="Show All", command=self.load_tasks)
        self.show_all_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        print("Adding task")
        task_description = self.entry.get()
        if task_description:
            self.todo_list.add_task(task_description)
            self.entry.delete(0, tk.END)
            self.load_tasks()

    def edit_task(self):
        print("Editing task")
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_number = selected_task_index[0] + 1
            task = self.todo_list.tasks[task_number - 1]
            new_description = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task.description)
            if new_description:
                task.description = new_description
                self.todo_list.save_tasks()
                self.load_tasks()

    def complete_task(self):
        print("Completing task")
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_number = selected_task_index[0] + 1
            self.todo_list.mark_task_completed(task_number)
            self.load_tasks()

    def delete_task(self):
        print("Deleting task")
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_number = selected_task_index[0] + 1
            self.todo_list.remove_task(task_number)
            self.load_tasks()

    def load_tasks(self):
        print("Loading tasks")
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def sort_by_name(self):
        print("Sorting tasks by name")
        self.todo_list.tasks.sort(key=lambda task: task.description)
        self.load_tasks()

    def sort_by_status(self):
        print("Sorting tasks by status")
        def compare(task1, task2):
            if task1.completed == task2.completed:
                return 0
            elif task1.completed:
                return 1
            else:
                return -1
        self.todo_list.tasks.sort(key=cmp_to_key(compare))
        self.load_tasks()

    def filter_completed(self):
        print("Filtering completed tasks")
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            if task.completed:
                self.task_listbox.insert(tk.END, str(task))

    def filter_incomplete(self):
        print("Filtering incomplete tasks")
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            if not task.completed:
                self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    print("Starting ToDoApp")
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
