class Traduction_En:
    # Tous les print sont du bas niveau
    def __init__(self, time):
        self.time = time

    # Moyen niveau
    def greeting(self):
        if self.time < 12:
            print("Good morning!")
        elif self.time > 12 and self.time < 20:
            print("Good afternoon!")
        else:
            print("Good evenning!")
        print("Enter a word to reverse")

    # Moyen niveau
    def goodbye(self):
        print("Goodbye!")

    # Moyen niveau
    def palindromeFound(self):
        print("Well said!")
