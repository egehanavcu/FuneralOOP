class Funeral:
    def __init__(self, deceased, family_members, cemetery, services):
        self.deceased = deceased
        self.family_members = family_members
        self.cemetery = cemetery
        self.services = services

    def hold_funeral(self):
        print("--- Deceased Information ---")
        print(f"Deceased Name: {self.deceased.name}")
        print(f"Date of Death: {self.deceased.date_of_death}")
        print(f"Cause of Death: {self.deceased.cause_of_death}")
        print(f"Funeral Cemetery: {self.cemetery.name} - {self.cemetery.address}")

        print("\n--- Family Members ---")
        for member in self.family_members:
            print(f"Name: {member.name}, Age: {member.age}, Relation: {member.relation}")
            
        print("\n--- Services ---")
        for service in self.services:
            print(service.perform())