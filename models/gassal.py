from models.person import Person

class Gassal(Person):
    def __init__(self, name, age, experience_years):
        super().__init__(name, age)
        self.experience_years = experience_years

    def get_role(self):
        return "Gassal"

    def wash_body(self):
        return f"{self.name} ({self.experience_years} years of experience) washed the body."