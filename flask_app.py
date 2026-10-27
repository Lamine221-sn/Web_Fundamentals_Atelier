from flask import Flask, render_template, request
from flask import Flask, render_template
# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")

# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{a} + {b} = {a + b}"

@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Lamine", nom="Mbengue")

@app.get("/loisirs")
def loisir():
    return ("J'aime le Football."
            "J'aime l'embrayage des boites mecaniques, faire du drift et les M4 G82")
    return render_template("presentation.html", prenom="Lamine", nom="Mbengue",
                       loisirs=["Jeux vidéo", "Musique", "Escalade","BMW"])
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return f"<h1>Bonjour {prenom} !</h1>"

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.get("/salut")
def salut():
    prenom = request.args.get("prenom", "inconnu")
    ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} !"

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
