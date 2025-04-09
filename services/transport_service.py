from services.base import Service

class TransportService(Service):
    def __init__(self, plate_number, price):
        super().__init__(price)
        self.plate_number = plate_number
           
    def perform(self):
        return f"Transportation was completed with vehicle plate number {self.plate_number}."