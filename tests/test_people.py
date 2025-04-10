import unittest
from people.person import Person
from people.deceased import Deceased
from people.gassal import Gassal
from people.imam import Imam
from people.attendee import Attendee

class TestPeople(unittest.TestCase):
    def test_person(self):
        person = Person("Ayşe Yılmaz", 73)
        self.assertEqual(person.name, "Ayşe Yılmaz")
        self.assertEqual(person.age, 73)

    def test_deceased(self):
        deceased = Deceased("Ahmet Yılmaz", 75, "09.04.2025", "Heart Attack")
        self.assertEqual(deceased.name, "Ahmet Yılmaz")
        self.assertEqual(deceased.age, 75)
        self.assertEqual(deceased.date_of_death, "09.04.2025")
        self.assertEqual(deceased.cause_of_death, "Heart Attack")

    def test_gassal(self):
        gassal = Gassal("Eda Gassal", 40, 11)
        self.assertEqual(gassal.name, "Eda Gassal")
        self.assertEqual(gassal.age, 40)
        self.assertEqual(gassal.experience_years, 11)
        self.assertIn("washed the body", gassal.wash_body())

    def test_imam(self):
        imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
        self.assertEqual(imam.name, "Hüseyin Hodja")
        self.assertEqual(imam.age, 55)
        self.assertEqual(imam.mosque, "Istanbul Mosque")
        self.assertIn("has prayed", imam.pray())

    def test_attendee(self):
        attendee = Attendee("Emre Demir", 72, "Friend", False, "I'm truly sorry for your loss.")
        self.assertEqual(attendee.name, "Emre Demir")
        self.assertEqual(attendee.age, 72)
        self.assertEqual(attendee.relation, "Friend")
        self.assertEqual(attendee.is_relative, False)
        self.assertIn("I'm truly sorry for your loss.", attendee.say_condolence())