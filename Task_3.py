todo_list = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = todo_list.pop(task_no - 1)
        print(f"Removed task: {removed}")
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
