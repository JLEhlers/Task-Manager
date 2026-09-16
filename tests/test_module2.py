import unittest

from business_logic import BusinessLogic
from models import Task


class TestAddTask(unittest.TestCase):
    """Test the add task use case."""

    def setUp(self):
        """Set up tasks for testing."""

        self.business = BusinessLogic()

        self.tasks = [
            Task(
                "john",
                "Task 1",
                "Complete assignment",
                "2026-09-10",
                "2026-09-07"
            )
        ]

    def test_add_task(self):
        """Test that a new task is added."""

        new_task = Task(
            "john",
            "Task 2",
            "Write unit tests",
            "2026-09-15",
            "2026-09-07"
        )

        self.business.add_task(self.tasks, new_task)

        self.assertEqual(len(self.tasks), 2)
        self.assertEqual(self.tasks[-1].title, "Task 2")


if __name__ == "__main__":
    unittest.main()
