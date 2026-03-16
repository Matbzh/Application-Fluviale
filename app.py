from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculer", methods= ["POST"])
def calculer():
    # Récuparation des données du formulaire
    volume_transporte = float(request.form["volume_transporte"])
    volume_embarcation = float(request.form["volume_embarcation"])
    distance_fluviale = float(request.form["distance_fluviale"])
    distance_routiere = float(request.form["distance_routiere"])
    type_embarcation = request.form["type_embarcation"]
    voie_deau = request.form["voie_deau"]
    sens_circulation = request.form["sens_circulation"]

    # Renvoyer les données reçu pour vérification.
    return f"Volume transporté : {volume_transporte} tonnes"

app.run(debug=True)