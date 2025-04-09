from models.person import Person

class Imam(Person):
    def __init__(self, name, age, mosque):
        super().__init__(name, age)
        self.mosque = mosque

    def get_role(self):
        return "İmam"