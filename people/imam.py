from people.person import Person

class Imam(Person):
    def __init__(self, name, age, mosque):
        super().__init__(name, age)
        self.mosque = mosque

    def pray(self):
        return f"{self.name} has prayed to god."