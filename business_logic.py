# import the necessary modules
from data_access import DataAccess


class BusinessLogic:
    """Handles the rules and operations of the task manager."""

    def __init__(self):
        self.data = DataAccess()

    def login(self, username, password):
        """Check whether the login details are correct."""

        users = self.data.get_users()

        for user in users:
            if user.username == username and user.password == password:
                return user

        return None

    def add_task(self, task):
        """Add a task to the task list."""

        tasks = self.data.get_tasks()

        tasks.append(task)

        self.data.save_tasks(tasks)

    def complete_task(self, task):
        """Mark a task as completed."""

        task.completed = "Yes"

        tasks = self.data.get_tasks()

        self.data.save_tasks(tasks)
