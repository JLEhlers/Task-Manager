from constants import TASK_FILE, USER_FILE
from models import Task, User


class DataAccess:
    """Handles reading and writing data to files."""

    def get_users(self):
        """Read users from user.txt."""
        users = []

        with open(USER_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(", ")
                users.append(User(username, password))

        return users

    def save_user(self, user):
        """Save a new user to user.txt."""
        with open(USER_FILE, "a") as file:
            file.write(
                f"{user.username}, {user.password}\n"
            )

    def get_tasks(self):
        """Read tasks from tasks.txt."""
        tasks = []

        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(", ")

                task = Task(
                    parts[0],
                    parts[1],
                    parts[2],
                    parts[3],
                    parts[4],
                    parts[5]
                )

                tasks.append(task)

        return tasks

    def save_tasks(self, tasks):
        """Save tasks to tasks.txt."""
        with open(TASK_FILE, "w") as file:
            file.writelines(
                f"{task.assigned_to}, "
                f"{task.title}, "
                f"{task.description}, "
                f"{task.due_date}, "
                f"{task.current_date}, "
                f"{task.completed}\n"
                for task in tasks
            )
