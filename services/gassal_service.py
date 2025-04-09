from services.base import Service
       
class GassalService(Service):
    def __init__(self, gassal, price):
        super().__init__(price)
        self.gassal = gassal
           
    def perform(self):
        return self.gassal.wash_body()