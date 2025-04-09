from services.base import Service

class ImamService(Service):
    def __init__(self, imam, price):
        super().__init__(price)
        self.imam = imam

    def perform(self):
        return self.imam.pray()