class Traduction_Fr:
    # Tous les print sont du bas niveau
    def __init__(self, time):
        self.time = time

    # Moyen niveau
    def greeting(self):
        if self.time > 6 and self.time < 20:
            print("Bonjour !")
        else:
            print("Bonsoir !")
        print("Entrez un mot à inverser:")

    # Moyen niveau
    def goodbye(self):
        if self.time > 6 and self.time < 20:
            print("Bonne journée !")
        else:
            print("Bonne soirée !")

    # Moyen niveau
    def palindromeFound(self):
        print("Bien dit !")
