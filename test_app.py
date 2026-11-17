import unittest
from app import main, welcome_message

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(main(), "Hello, DevOps!")

    def test_return_type(self):
        self.assertIsInstance(main(), str)

    def test_welcome_message(self):
        self.assertEqual(welcome_message("Rahul"), "Welcome to DevOps, Rahul!")
        self.assertEqual(welcome_message("Aman"), "Welcome to DevOps, Aman!")

if __name__ == "__main__":
    unittest.main()
