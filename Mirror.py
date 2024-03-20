from datetime import datetime


class Mirror:

    def __init__(self, langue):
        self.langue = langue
        self.mot = ""

    def greeting(self):
        moment = datetime.now().time().hour
        if moment < 12:
            print("Good morning!")
        elif moment > 12 and moment < 20:
            print("Good afternoon!")
        else:
            print("Good evenning!")
        print("Enter a word to reverse")

    def goodbye(self):
        print("Goodbye!")

    def mirror(self):
        nouveau_mot = self.mot[::-1]
        if (self.mot == nouveau_mot):
            print("Well said!")
        else:
            print(nouveau_mot)

    def getInput(self):
        self.mot = input()
