from abc import ABC, abstractmethod


class Lang(ABC):

    @abstractmethod
    def greeting(self, time):
        pass

    @abstractmethod
    def goodbye(self, time):
        pass

    @abstractmethod
    def greetingMorning(self):
        pass

    @abstractmethod
    def greetingAfternoon(self):
        pass

    @abstractmethod
    def greetingEvenning(self):
        pass

    @abstractmethod
    def goodbyeDefault(self):
        pass

    @abstractmethod
    def goodbyeEvenning(self):
        pass

    @abstractmethod
    def palindromeFound(self):
        pass
