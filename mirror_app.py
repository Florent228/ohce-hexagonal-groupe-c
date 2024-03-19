
# mirror_app.py

from greeter import Greeter
from language_support import LanguageSupport

class MirrorApp:
    """Application principale pour renvoyer en miroir les entrées et reconnaître les palindromes."""
    
    def __init__(self, language='en'):
        self.language = language
        self.greeter = Greeter(language)
    
    def start(self):
        """Démarre l'application avec un message de salutation."""
        print(self.greeter.greet())
    
    def run(self):
        """Boucle principale de l'application."""
        try:
            while True:
                user_input = input(LanguageSupport.get_message(self.language, 'prompt'))
                if user_input.lower() == 'exit':
                    print(self.greeter.farewell())
                    break
                self.process_input(user_input)
        except KeyboardInterrupt:
            print("\n" + self.greeter.farewell())
    
    def process_input(self, user_input):
        """Traite l'entrée utilisateur, vérifie les palindromes et renvoie en miroir."""
        if user_input == user_input[::-1]:
            print(LanguageSupport.get_message(self.language, 'well_said'))
        else:
            print(user_input)

if __name__ == "__main__":
    language = input(LanguageSupport.get_message('en', 'choose_language'))  # Default to English for initial prompt
    app = MirrorApp(language)
    app.start()
    app.run()
