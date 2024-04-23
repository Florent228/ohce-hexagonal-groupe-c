from abc import ABC, abstractmethod

class Horloge(ABC):
    @abstractmethod
    def getHour(self):
        pass
