from Traduction_En import Traduction_En
from Traduction_Fr import Traduction_Fr
import locale


class Langue:
    def __init__(self, time):
        self.time = time

    @staticmethod
    # Haut niveau
    def getSystemLanguageLocale():
        # Bas niveau, interaction avec l'OS
        langue_locale = locale.getlocale()[0]
        # Split, bas niveau
        code_langue = langue_locale.split('_')[0]
        return code_langue

    # Haut niveau
    def getLanguage(self):
        # Bas niveau
        code_language = self.getSystemLanguageLocale()
        # Bas niveau
        language = Traduction_En(
            self.time) if code_language == 'en' else Traduction_Fr(self.time)
        return language
