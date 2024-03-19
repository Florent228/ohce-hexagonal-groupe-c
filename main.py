import sys
from mirror_app import MirrorApp
from api_wrapper import app as flask_app

def start_console_app(language):
    """Démarre l'application en mode console."""
    app = MirrorApp(language=language)
    app.start()
    app.run()

def start_api():
    """Démarre l'application en tant qu'API REST."""
    flask_app.run(debug=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == 'api':
            print("Démarrage de l'application en mode API REST...")
            start_api()
        elif mode == 'console':
            language = 'en'  # Défaut à l'anglais, peut être modifié ou rendu configurable
            print("Démarrage de l'application en mode console...")
            start_console_app(language)
        else:
            print("Mode non reconnu. Veuillez choisir 'api' ou 'console'.")
    else:
        print("Aucun mode spécifié. Usage: main.py [api|console]")
