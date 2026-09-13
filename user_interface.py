class UserInterface:
    """Handles user input and output."""

    def get_username(self):
        return input("Enter your username: ")

    def get_password(self):
        return input("Enter your password: ")

    def show_task(self, task):
        print("-" * 50)
        print(f"{'Title:':15}{task.title}")
        print(f"{'Assigned to:':15}{task.assigned_to}")
        print(f"{'Assigned:':15}{task.current_date}")
        print(f"{'Due:':15}{task.due_date}")
        print(f"{'Completed:':15}{task.completed}")
        print(f"{'Description:':15}{task.description}")
        print("-" * 50)
