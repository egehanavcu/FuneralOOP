from models.deceased import Deceased
from models.family_member import FamilyMember
from models.imam import Imam
from models.gassal import Gassal
from models.cemetery import Cemetery

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