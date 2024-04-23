from langs.Traduction_En import Traduction_En
from langs.Traduction_Fr import Traduction_Fr

class LangFactory:

    def create_lang(self, code_langue):
        match code_langue:
            case 'fr':
                return Traduction_Fr()
            case 'en':
                return Traduction_En()
            case _:
                return Traduction_En()
