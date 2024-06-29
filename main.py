from to_do_list import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo Do List:")
        todo_list.display_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            task_number = int(input("Enter task number to mark completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '3':
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
