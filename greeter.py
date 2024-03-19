# greeter.py

from datetime import datetime

class Greeter:
    """Classe pour gérer les salutations selon le moment de la journée et la langue."""
    
    greetings = {
        'fr': {'morning': 'Bonjour', 'evening': 'Bonsoir', 'night': 'Bonne nuit', 'farewell': 'Au revoir'},
        'en': {'morning': 'Good morning', 'evening': 'Good evening', 'night': 'Good night', 'farewell': 'Goodbye'},
        # Ajouter d'autres langues ici
    }
    
    def __init__(self, language='en'):
        self.language = language
    
    def greet(self):
        """Renvoie une salutation basée sur le moment de la journée."""
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            return self.greetings[self.language]['morning']
        elif 12 <= current_hour < 18:
            return self.greetings[self.language]['evening']
        else:
            return self.greetings[self.language]['night']
    
    def farewell(self):
        """Renvoie un message d'adieu."""
        return self.greetings[self.language]['farewell']

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
