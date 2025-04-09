from people.person import Person

class Attendee(Person):
    def __init__(self, name, age, relation, is_relative=False):
        super().__init__(name, age)
        self.relation = relation
        self.is_relative = is_relative