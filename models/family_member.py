from models.person import Person

class FamilyMember(Person):
    def __init__(self, name, age, relation):
        super().__init__(name, age)
        self.relation = relation