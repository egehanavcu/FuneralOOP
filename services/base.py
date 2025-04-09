from abc import ABC, abstractmethod

class Service(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def perform(self):
        pass