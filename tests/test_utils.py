import unittest
from utils import random_condolence_message

class TestUtils(unittest.TestCase):
    def test_random_condolence_message(self):
        message = random_condolence_message()
        self.assertIsInstance(message, str)
        self.assertGreater(len(message), 0)