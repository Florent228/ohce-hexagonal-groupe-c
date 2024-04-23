from domain.HorlogeSysteme import HorlogeSysteme
from console.LangUtilities import getSystemLanguageLocale
from langs.LangFactory import LangFactory
from console.MirrorConsole import MirrorConsole
from domain.MirrorService import MirrorService

time = HorlogeSysteme()
langue_factory = LangFactory()
language = langue_factory.create_lang(getSystemLanguageLocale())
mirror_service = MirrorService(language, time)
mirror = MirrorConsole(mirror_service)
mirror.mirrorWord()
