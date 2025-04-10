import unittest
from services.gassal_service import GassalService
from services.imam_service import ImamService
from services.transport_service import TransportService
from people.gassal import Gassal
from people.imam import Imam

class TestServices(unittest.TestCase):
    def test_gassal_service(self):
        gassal = Gassal("Eda Gassal", 40, 11)
        service = GassalService(gassal, 400)
        self.assertEqual(service.price, 400)
        self.assertIn("washed the body", service.perform())

    def test_imam_service(self):
        imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
        service = ImamService(imam, 500)
        self.assertEqual(service.price, 500)
        self.assertIn("has prayed", service.perform())

    def test_transport_service(self):
        service = TransportService("49 SVR 0961", 700)
        self.assertEqual(service.plate_number, "49 SVR 0961")
        self.assertEqual(service.price, 700)
        self.assertIn("Transportation was completed", service.perform())