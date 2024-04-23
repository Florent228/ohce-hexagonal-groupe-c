from Lang import Lang
from MirrorConsole import MirrorConsole
from MirrorService import MirrorService
from Horloge import Horloge


# Haut niveau
time = Horloge.getHour()
langue = Lang(time).getLanguage()
mirror_service = MirrorService(langue)
mirror = MirrorConsole(mirror_service)
mirror.mirrorWord()
