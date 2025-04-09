from people.person import Person
from utils import random_condolence_message

class Attendee(Person):
    def __init__(self, name, age, relation, is_relative=False, condolence_message=None):
        super().__init__(name, age)
        self.relation = relation
        self.is_relative = is_relative
        self.condolence_message = condolence_message or random_condolence_message()

    def say_condolence(self):
        return f"{self.name} says: {self.condolence_message}"