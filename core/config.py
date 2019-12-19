from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# creo un'istanza della mia applicazione flask



# configuro la chiave segreta che serve per gestire la sessione degli utenti loggati
app.secret_key = 'super-secret-key'


# configuro il database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.sqlite"

db = SQLAlchemy(app)
db.init_app(app)

db.create_all()

migrate = Migrate(app, db)

from core.controllers.esercizio.esercizioController import esercizio_bp
from core.controllers.main.mainController import main
app.register_blueprint(main)
app.register_blueprint(esercizio_bp, url_prefix="/esercizio")









