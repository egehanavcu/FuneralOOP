class Funeral:
    def __init__(self, deceased, attendees, cemetery, services):
        self.deceased = deceased
        self.attendees = attendees
        self.cemetery = cemetery
        self.services = services

    def hold_funeral(self):
        self._print_deceased_info()
        self._print_attendees()
        self._print_condolences()
        self._perform_services()
        self._print_total_cost()

    def _print_deceased_info(self):
        print("--- Deceased Information ---")
        print(f"Deceased Name: {self.deceased.name}")
        print(f"Date of Death: {self.deceased.date_of_death}")
        print(f"Cause of Death: {self.deceased.cause_of_death}")
        print(f"Funeral Cemetery: {self.cemetery.name} - {self.cemetery.address}")

    def _print_attendees(self):
        relatives = [a for a in self.attendees if a.is_relative]
        non_relatives = [a for a in self.attendees if not a.is_relative]

        print("\n--- Family Members ---")
        for member in relatives:
            print(f"Name: {member.name}, Age: {member.age}, Relation: {member.relation}")

        print("\n--- Other Attendees ---")
        for member in non_relatives:
            print(f"Name: {member.name}, Age: {member.age}, Relation: {member.relation}")

    def _print_condolences(self):
        print("\n--- Condolence Messages ---")
        for attendee in self.attendees:
            print(attendee.say_condolence())

    def _perform_services(self):
        print("\n--- Services ---")
        for service in self.services:
            print(service.perform())

    def _print_total_cost(self):
        print("\nTotal Cost of the Funeral:", self.calculate_total_cost(), "Turkish Liras.")

    def calculate_total_cost(self):
        return sum(service.price for service in self.services)