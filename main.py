from people.deceased import Deceased
from people.attendee import Attendee
from people.imam import Imam
from people.gassal import Gassal
from services import ImamService, GassalService, TransportService
from funeral import Funeral
from cemetery import Cemetery

if __name__ == "__main__":
    deceased = Deceased("Ahmet Yılmaz", 75, "09.04.2025", "Heart Attack")
    attendees = [
        Attendee("Ayşe Yılmaz", 73, "Wife", True),
        Attendee("Mehmet Yılmaz", 50, "Son", True),
        Attendee("Fatma Kaya", 48, "Daughter", True),
        Attendee("Emre Demir", 72, "Friend"),
        Attendee("Emir Çelik", 74, "Friend")
    ]
    imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
    gassal = Gassal("Eda Gassal", 40, 11)
    cemetery = Cemetery("Zincirlikuyu Cemetery", "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")

    imam_service = ImamService(imam, 500)
    gassal_service = GassalService(gassal, 400)
    transport_service = TransportService("49 SVR 0961", 700)

    funeral = Funeral(deceased, attendees, cemetery, [imam_service, gassal_service, transport_service])
    funeral.hold_funeral()