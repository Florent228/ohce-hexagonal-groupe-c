class Mirror:
    def __init__(self, langue):
        self.langue = langue
        self.mot = ""

    def getInput(self):
        self.mot = input()

    def mirror(self):
        self.langue.greeting()
        nouveau_mot = self.mot[::-1]
        if (self.mot == nouveau_mot):
            self.langue.isPalindrome()
        else:
            print(nouveau_mot)
