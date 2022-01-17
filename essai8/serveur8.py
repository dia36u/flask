from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/bonjour', methods=['POST'])
def hello():
    resultat = request.form
    nom = resultat['Nom']
    prenom = resultat['Prénom']
    meteo = resultat['meteo']
    nomComplet = nom + " " + prenom
    return render_template("bonjour.html" , message = nomComplet, meteo=meteo)
app.run()

