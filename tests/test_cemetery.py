import unittest
from cemetery import Cemetery

class TestCemetery(unittest.TestCase):
    def test_cemetery(self):
        cemetery = Cemetery("Zincirlikuyu Cemetery", "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")
        self.assertEqual(cemetery.name, "Zincirlikuyu Cemetery")
        self.assertEqual(cemetery.address, "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")