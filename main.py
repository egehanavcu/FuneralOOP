from people.deceased import Deceased
from people.imam import Imam
from people.gassal import Gassal
from services import ImamService, GassalService, TransportService
from funeral import Funeral
from cemetery import Cemetery

if __name__ == "__main__":
    deceased = Deceased("Ahmet Yılmaz", 75, "09.04.2025", "Heart Attack")

    imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
    gassal = Gassal("Eda Gassal", 40, 11)
    cemetery = Cemetery("Zincirlikuyu Cemetery", "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")

    funeral = (
        Funeral(deceased)
        .set_cemetery(cemetery)
        .add_attendee("Ayşe Yılmaz", 73, "Wife", True)
        .add_attendee("Mehmet Yılmaz", 50, "Son", True)
        .add_attendee("Fatma Kaya", 48, "Daughter", True)
        .add_attendee("Emre Demir", 72, "Friend")
        .add_attendee("Emir Çelik", 74, "Friend")
        .add_service(ImamService(imam, 500))
        .add_service(GassalService(gassal, 400))
        .add_service(TransportService("49 SVR 0961", 700))
    )
    
    funeral.hold_funeral()