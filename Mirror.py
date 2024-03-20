class Mirror:

    def __init__(self, langue):
        self.langue = langue
        self.mot = ""

    # Moyen niveau
    def getInput(self):
        # Input --> Bas niveau
        self.mot = input()

    # Haut niveau
    def mirror(self):
        # greeting, moyen niveau
        self.langue.greeting()
        self.getInput()
        # Slicing, bas niveau
        nouveau_mot = self.mot[::-1]
        if (self.mot == nouveau_mot):
            # Moyen niveau
            self.langue.palindromeFound()
        else:
            # Bas niveau
            print(nouveau_mot)
        # Moyen niveau
        self.langue.goodbye()
