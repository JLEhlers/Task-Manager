class User:
    """Represents a user."""

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Task:
    """Represents a task."""

    def __init__(
        self,
        assigned_to,
        title,
        description,
        due_date,
        current_date,
        completed="No"
    ):
        self.assigned_to = assigned_to
        self.title = title
        self.description = description
        self.due_date = due_date
        self.current_date = current_date
        self.completed = completed
