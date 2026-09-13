import unittest

from business_logic import BusinessLogic
from models import Task


class TestDeleteTask(unittest.TestCase):
    """Test the delete task use case."""

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
            ),
            Task(
                "mary",
                "Task 2",
                "Finish project",
                "2026-09-15",
                "2026-09-07"
            )
        ]

    def test_delete_task(self):
        """Test that a task can be deleted."""

        result = self.business.delete_task(
            self.tasks,
            "Task 1"
        )

        self.assertTrue(result)
        self.assertEqual(len(self.tasks), 1)

    def test_delete_task_not_found(self):
        """Test deleting a task that does not exist."""

        result = self.business.delete_task(
            self.tasks,
            "Task 99"
        )

        self.assertFalse(result)
        self.assertEqual(len(self.tasks), 2)


if __name__ == "__main__":
    unittest.main()
