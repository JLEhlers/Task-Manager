class BusinessLogic:
    """Handles the rules of the task manager."""

    def login(self, users, username, password):
        """Check if the login details are correct."""

        for user in users:
            if user.username == username and user.password == password:
                return user

        return None

    def add_task(self, tasks, task):
        """Add a new task."""

        tasks.append(task)

        return tasks

    def complete_task(self, task):
        """Mark a task as completed."""

        task.completed = "Yes"

        return task

    def delete_task(self, tasks, task_title):
        """Delete a task by its title."""

        for task in tasks:
            if task.title == task_title:
                tasks.remove(task)
                return True

        return False
