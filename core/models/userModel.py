from core.config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = db.Column(db.String, nullable=False)
    user_surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
