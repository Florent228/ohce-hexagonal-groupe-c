from langs.Lang import Lang

class Traduction_Fr(Lang):
    
    def greeting(self, time: int):
        if time < 12:
            return self.greetingMorning()
        return self.greetingEvenning()
            
    def goodbye(self, time: int):
        if time > 6 and time < 20:
            return self.goodbyeDefault()
        return self.goodbyeEvenning()

    def greetingMorning(self):
        return "Bonjour !"

    def greetingAfternoon(self):
        return self.greetingMorning()

    def greetingEvenning(self):
        return "Bonsoir !"

    def goodbyeDefault(self):
        return "Au revoir bonne journée !"

    def goodbyeEvenning(self):
        return "Au revoir bonne soirée !"

    def palindromeFound(self):
        return "Bien dit !"
