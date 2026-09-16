from business_logic import BusinessLogic
from models import Task
from utilities import get_current_date


def start_application():
    """Start the Task Management Application."""

    business = BusinessLogic()
    tasks = []

    while True:
        print("\nTask Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks, business)

        elif choice == "3":
            complete_task(tasks, business)

        elif choice == "4":
            delete_task(tasks, business)

        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def view_tasks(tasks):
    """Display all tasks."""

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for task in tasks:
        print(f"- {task.title}")
        print(f"  Assigned to: {task.assigned_to}")
        print(f"  Description: {task.description}")
        print(f"  Due date: {task.due_date}")
        print(f"  Completed: {task.completed}")


def add_task(tasks, business):
    """Get task details and add a new task."""

    assigned_to = input("Enter username: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    current_date = get_current_date()

    new_task = Task(
            assigned_to,
            title,
            description,
            due_date,
            current_date
        )

    business.add_task(tasks, new_task)

    print("Task added successfully!")


def complete_task(tasks, business):
    """Mark a task as completed."""

    title = input("Enter the task title to complete: ")

    for task in tasks:
        if task.title == title:
            business.complete_task(task)
            print("Task completed successfully!")
            return

    print("Task not found.")


def delete_task(tasks, business):
    """Delete a task."""

    title = input("Enter the task title to delete: ")

    result = business.delete_task(tasks, title)

    if result:
        print("Task deleted successfully!")
    else:
        print("Task not found.")
