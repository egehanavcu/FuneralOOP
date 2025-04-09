class Funeral:
    def __init__(self, deceased, attendees, cemetery, services):
        self.deceased = deceased
        self.attendees = attendees
        self.cemetery = cemetery
        self.services = services

    def hold_funeral(self):
        print("--- Deceased Information ---")
        print(f"Deceased Name: {self.deceased.name}")
        print(f"Date of Death: {self.deceased.date_of_death}")
        print(f"Cause of Death: {self.deceased.cause_of_death}")
        print(f"Funeral Cemetery: {self.cemetery.name} - {self.cemetery.address}")

        relatives = [attendee for attendee in self.attendees if attendee.is_relative]
        non_relatives = [attendee for attendee in self.attendees if not attendee.is_relative]

        print("\n--- Family Members ---")
        for member in relatives:
            print(f"Name: {member.name}, Age: {member.age}, Relation: {member.relation}")

        print("\n--- Other Attendees ---")
        for member in non_relatives:
            print(f"Name: {member.name}, Age: {member.age}, Relation: {member.relation}")

        print("\n--- Services ---")
        for service in self.services:
            print(service.perform())

        print("\nTotal Cost of the Funeral:", self.calculate_total_cost(), "Turkish Liras.")

    def calculate_total_cost(self):
        return sum(service.price for service in self.services)