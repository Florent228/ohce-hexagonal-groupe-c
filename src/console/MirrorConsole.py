from domain.MirrorService import MirrorService

class MirrorConsole:

    def __init__(self, mirror_service: MirrorService):
        self.mirror_service = mirror_service

    def getInput(self):

        self.mirror_service.getWord(input())

    def mirrorWord(self):
        print(self.mirror_service.greeting())
        self.getInput()
        print(self.mirror_service.mirror())
        print(self.mirror_service.goodbye())
