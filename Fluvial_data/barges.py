import pandas as pd

# Caractéristiques des unités fluviales
# Colonnes : Type de cale, Longueur (m), Capacité d'emport (t), Nombre de balles

# Automoteurs
Automoteur_Caracteristiques = pd.DataFrame([
    ["Freycinet limité", 39, 250, 207],
    ["Freycinet plein", 39, 400, 207],
    ["Marnemax", 45, 440, 276],
    ["Canal du nord", 72, 800, 504],
    ["Convoi freycinet en flèche", 78, 800, 414],
    ["DEK", 80, 800, None],
    ["Convoi Marnemax en flèche", 90, 880, 552]
], columns=["Type de cale", "Longueur", "Capacité d'emport (t)", "Nombre de balles"])

# Pousseurs
Pousseur_Caracteristiques = pd.DataFrame([
    ["Convoi 110m", 110, 2500, None],
    ["Convoi 180m", 180, 5000, None]
], columns=["Type de cale", "Longueur", "Capacité d'emport (t)", "Nombre de balles"])