class Traduction_Fr:

    def __init__(self, time):
        self.time = time

    def greeting(self):
        if self.time > 6 and self.time < 20:
            print("Bonjour !")
        else:
            print("Bonsoir !")
        print("Enter a word to reverse")

    def goodbye(self):
        if self.time > 6 and self.time < 20:
            print("Bonne journée !")
        else:
            print("Bonne soirée !")

    def isPalindrome(self):
        print("Bien dit !")
