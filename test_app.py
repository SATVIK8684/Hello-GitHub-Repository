import unittest
from app import main

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(main(), "Hello, Git!")

if __name__ == "__main__":
    unittest.main()
