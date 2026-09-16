import unittest

from business_logic import BusinessLogic
from models import User


class TestLogin(unittest.TestCase):
    """Test the user login use case."""

    def setUp(self):
        """Set up users for testing."""

        self.business = BusinessLogic()

        self.users = [
            User("john", "password123"),
            User("mary", "password456")
        ]

    def test_login_successful(self):
        """Test that valid login details work."""

        result = self.business.login(
            self.users,
            "john",
            "password123"
        )

        self.assertIsNotNone(result)
        self.assertEqual(result.username, "john")

    def test_login_invalid_password(self):
        """Test that an incorrect password fails."""

        result = self.business.login(
            self.users,
            "john",
            "wrongpassword"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
