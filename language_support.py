# language_support.py

class LanguageSupport:
    """Classe pour gérer le support multilingue et les messages spécifiques à chaque langue."""
    
    messages = {
        'fr': {
            'prompt': "Écrivez quelque chose (ou 'exit' pour quitter) : ",
            'well_said': "Bien dit !",
            'choose_language': "Choisissez votre langue (fr/en) : "
        },
        'en': {
            'prompt': "Type something (or 'exit' to quit): ",
            'well_said': "Well said!",
            'choose_language': "Choose your language (fr/en): "
        },
        # Ajouter d'autres langues ici
    }
    
    @staticmethod
    def get_message(language, message_key):
        """Renvoie le message demandé dans la langue spécifiée."""
        return LanguageSupport.messages.get(language, {}).get(message_key, "")
