from domain.HorlogeSysteme import HorlogeSysteme
from langs import Lang

class MirrorService:

    def __init__(self, langue: Lang, time: HorlogeSysteme):
        self.langue = langue
        self.mot = ""
        self.time = time

    def getWord(self, mot):
        self.mot = mot

    def mirror(self):
        nouveau_mot = self.mot[::-1]
        if self.mot == nouveau_mot:
            return nouveau_mot + "\n" + self.langue.palindromeFound()
        return nouveau_mot

    def greeting(self):
        return self.langue.greeting(self.time.getHour())

    def goodbye(self):
        return self.langue.goodbye(self.time.getHour())
