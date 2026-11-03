import unittest
from app import main

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(main(), "Hello, DevOps!")

    def test_return_type(self):
        self.assertIsInstance(main(), str)

if __name__ == "__main__":
    unittest.main()
