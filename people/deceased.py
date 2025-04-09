from people.person import Person

class Deceased(Person):
    def __init__(self, name, age, date_of_death, cause_of_death):
        super().__init__(name, age)
        self.date_of_death = date_of_death
        self.cause_of_death = cause_of_death