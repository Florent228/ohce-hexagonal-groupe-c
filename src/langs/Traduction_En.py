from langs.Lang import Lang

class Traduction_En(Lang):

    def greeting(self, time: int):
        if time < 12:
            return self.greetingMorning()
        elif time > 12 and time < 20:
            return self.greetingAfternoon()
        else:
            return self.greetingEvenning()

    def goodbye(self, time):
        return self.goodbyeDefault()

    def greetingMorning(self):
        return "Good morning!"

    def greetingAfternoon(self):
        return "Good afternoon!"

    def greetingEvenning(self):
        return "Good evenning!"

    def goodbyeDefault(self):
        return "Goodbye!"

    def goodbyeEvenning(self):
        return self.goodbyeDefault()

    def palindromeFound(self):
        return "Well said!"
