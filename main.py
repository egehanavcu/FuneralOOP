from models.deceased import Deceased
from models.family_member import FamilyMember
from models.imam import Imam
from models.gassal import Gassal
from models.cemetery import Cemetery
from services.imam_service import ImamService
from services.gassal_service import GassalService
from services.transport_service import TransportService
from funeral import Funeral

if __name__ == "__main__":
    deceased = Deceased("Ahmet Yılmaz", 75, "09.04.2025", "Heart Attack")
    family = [
        FamilyMember("Ayşe Yılmaz", 73, "Wife"),
        FamilyMember("Mehmet Yılmaz", 50, "Son"),
        FamilyMember("Fatma Kaya", 48, "Daughter")
    ]
    imam = Imam("Hüseyin Hodja", 55, "Istanbul Mosque")
    gassal = Gassal("Eda Gassal", 40, 11)
    cemetery = Cemetery("Zincirlikuyu Cemetery", "Esentepe, Zincirlikuyu Cemetery, 34394 Sisli/Istanbul")

    imam_service = ImamService(imam, 500)
    gassal_service = GassalService(gassal, 400)
    transport_service = TransportService("49 SVR 0961", 700)

    funeral = Funeral(deceased, family, cemetery, [imam_service, gassal_service, transport_service])