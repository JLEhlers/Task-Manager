import unittest

from business_logic import BusinessLogic
from models import Task


class TestCompleteTask(unittest.TestCase):
    """Test the complete task use case."""

    def setUp(self):
        """Set up a task for testing."""

        self.business = BusinessLogic()

        self.task = Task(
            "john",
            "Task 1",
            "Complete assignment",
            "2026-09-10",
            "2026-09-07"
        )

    def test_complete_task(self):
        """Test that a task can be completed."""

        self.business.complete_task(self.task)

        self.assertEqual(self.task.completed, "Yes")


if __name__ == "__main__":
    unittest.main()
