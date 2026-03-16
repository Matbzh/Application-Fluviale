from flask import Flask, render_template, request
from calculs import calcul_fluvial, calcul_routier

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", resultats=False)

@app.route("/calculer", methods=["POST"])
def calculer():
    volume_transporte = float(request.form["volume_transporte"])
    volume_embarcation = float(request.form["volume_embarcation"])
    distance_fluviale = float(request.form["distance_fluviale"])
    distance_routiere = float(request.form["distance_routiere"])
    type_embarcation = request.form["type_embarcation"]
    voie_deau = request.form["voie_deau"]
    sens_circulation = request.form["sens_circulation"]

    resultats_fluviaux = calcul_fluvial(volume_transporte, volume_embarcation, distance_fluviale, type_embarcation, voie_deau, sens_circulation)
    resultats_routiers = calcul_routier(volume_transporte, distance_routiere)

    # Calcul du message de comparaison
    ges_fluvial = float(resultats_fluviaux["emissions_ges_t"])
    ges_routier = float(resultats_routiers["emissions_ges_t"])
    reduction = round((1 - ges_fluvial / ges_routier) * 100)
    message_comparaison = f"Le fluvial émet {reduction}% de moins que le routier"

    return render_template("index.html",
    resultats = True,
    # Paramètres saisis
    volume_transporte = volume_transporte,
    volume_embarcation = volume_embarcation,
    distance_fluviale = distance_fluviale,
    distance_routiere = distance_routiere,
    type_embarcation = type_embarcation,
    voie_deau = voie_deau,
    sens_circulation = sens_circulation,
    # Résultats
    tonne_km_fluvial = resultats_fluviaux["tonne_km"],
    consommation_L = round(float(resultats_fluviaux["consommation_L"])),
    emissions_co2_fluvial = round(float(resultats_fluviaux["emissions_co2_t"])),
    emissions_ges_fluvial = round(float(resultats_fluviaux["emissions_ges_t"])),
    tonne_km_routier = resultats_routiers["tonne_km"],
    emissions_ges_routier = round(float(resultats_routiers["emissions_ges_t"])),
    message_comparaison = message_comparaison
)

app.run(debug=True)