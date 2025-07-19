todo_list = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task Text")
    print("5. Mark Task as Done / Not Done")
    print("6. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, item in enumerate(todo_list, 1):
            status = "✓" if item["done"] else " "
            print(f"{i}. [{status}] {item['task']}")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = todo_list.pop(task_no - 1)
        print(f"Removed task: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid input.")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        new_text = input("Enter new task text: ")
        todo_list[task_no - 1]["task"] = new_text
        print("Task updated.")
    except (ValueError, IndexError):
        print("Invalid input.")

def mark_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark done/not done: "))
        current_status = todo_list[task_no - 1]["done"]
        todo_list[task_no - 1]["done"] = not current_status
        print(f"Task marked as {'done' if not current_status else 'not done'}.")
    except (ValueError, IndexError):
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        update_task()
    elif choice == '5':
        mark_task()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
