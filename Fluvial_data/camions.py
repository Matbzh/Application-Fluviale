import pandas as pd

# Caractéristiques des camions routiers
# Le volume est calculé automatiquement : Longueur × Largeur × Hauteur

# Données brutes (sans volume)
donnees_camions = [
    ["Camion benne", 13.4, 2.45, 2.60, 26, 27, "Camion articulé", "<34 tonnes"]
]

Camion_Caracteristiques = pd.DataFrame(donnees_camions, columns=[
    "Type de camion", 
    "Longueur", 
    "Largeur", 
    "Hauteur", 
    "Masse maximum transportée (t)", 
    "Nombre de balles transportées",
    "Désignation ADEME",
    "Classification masse ADEME"
])

# Calcul automatique du volume
Camion_Caracteristiques["Volume total (m3)"] = (
    Camion_Caracteristiques["Longueur"] * 
    Camion_Caracteristiques["Largeur"] * 
    Camion_Caracteristiques["Hauteur"]
).round(2)

# Réorganiser les colonnes dans l'ordre souhaité
Camion_Caracteristiques = Camion_Caracteristiques[[
    "Type de camion", "Longueur", "Largeur", "Hauteur", "Volume total (m3)",
    "Masse maximum transportée (t)", "Nombre de balles transportées",
    "Désignation ADEME", "Classification masse ADEME"
]]

# Vitesse de pré & post-acheminement