from flask import Blueprint, render_template, request

from core.config import db
from core.models.userModel import User

esercizio_bp = Blueprint("esercizio_bp", __name__)

@esercizio_bp.route("/inserisci_utente", methods=['GET','POST'])
def inserisci_utente():
    if request.method=="GET":
        return render_template('crea_utente.html') 
    elif request.method=="POST":   
        dati = request.form 
        nome_utente  = dati['nome_utente']
        cognome_utente = dati['cognome_utente']
        email = dati['email_utente']
        user =User(user_name=nome_utente, user_surname=cognome_utente, email=email)
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        return render_template("crea_utente.html", users=users)


