from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser la base de données
    db.init_app(app)

    # Créer les tables si elles n'existent pas
    with app.app_context():
        db.create_all()

    return app
