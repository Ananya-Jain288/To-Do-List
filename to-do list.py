import json

tasks = []

def add_task():
    task_name = input("Enter task: ")
    task = {
        "name": task_name,
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- TASK LIST ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - {task['status']}")

def complete_task():
    view_tasks()

    try:
        index = int(input("Enter task number to complete: ")) - 1
        tasks[index]["status"] = "Completed"
        print("Task marked as completed!")
    except:
        print("Invalid task number.")

def delete_task():
    view_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"{removed['name']} deleted.")
    except:
        print("Invalid task number.")

def search_task():
    keyword = input("Enter task name to search: ").lower()

    found = False

    for task in tasks:
        if keyword in task["name"].lower():
            print(task["name"], "-", task["status"])
            found = True

    if not found:
        print("Task not found.")

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        search_task()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")