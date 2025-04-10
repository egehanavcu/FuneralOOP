import unittest
from funeral import Funeral
from cemetery import Cemetery
from people.deceased import Deceased
from people.imam import Imam
from people.gassal import Gassal
from services.imam_service import ImamService
from services.gassal_service import GassalService
from services.transport_service import TransportService

class TestFuneral(unittest.TestCase):
    def setUp(self):
        self.deceased = Deceased("Ahmet Yılmaz", 75, "09.04.2025", "Heart Attack")
        self.imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
        self.gassal = Gassal("Eda Gassal", 40, 11)
        self.cemetery = Cemetery("Zincirlikuyu Cemetery", "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")
        self.funeral = Funeral(self.deceased).set_cemetery(self.cemetery)

    def test_set_cemetery(self):
        self.assertIsNotNone(self.funeral.cemetery)
        self.assertEqual(self.funeral.cemetery.name, "Zincirlikuyu Cemetery")
        self.assertEqual(self.funeral.cemetery.address, "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")

    def test_add_attendee(self):
        self.funeral.add_attendee("Ayşe Yılmaz", 73, "Wife", True)
        self.assertEqual(len(self.funeral.attendees), 1)
        self.assertEqual(self.funeral.attendees[0].name, "Ayşe Yılmaz")

    def test_add_service(self):
        service = ImamService(self.imam, 300)
        self.funeral.add_service(service)
        self.assertEqual(len(self.funeral.services), 1)

    def test_calculate_total_cost(self):
        self.funeral.add_service(ImamService(self.imam, 500))
        self.funeral.add_service(GassalService(self.gassal, 400))
        self.funeral.add_service(TransportService("49 SVR 0961", 700))
        self.assertEqual(self.funeral.calculate_total_cost(), 1600)

    def test_hold_funeral(self):
        self.funeral.add_attendee("Ayşe Yılmaz", 73, "Wife", True)
        self.funeral.add_service(ImamService(self.imam, 300))
        self.funeral.add_service(GassalService(self.gassal, 400))
        self.funeral.add_service(TransportService("34 DEF 567", 500))
        try:
            self.funeral.hold_funeral()
        except Exception as error:
            self.fail(f"hold_funeral error: {error}")