# Paramètres de calcul pour le transport

# Vitesses moyennes (km/h)
VITESSE_PRE_POST_ACHEMINEMENT = 30  # Vitesse camion pour pré/post-acheminement

# Facteurs d'émission fluvial
FACTEUR_EMISSION_FLUVIAL_CO2_DIESEL = 3.07  # kg CO2/L de diesel
FACTEUR_EMISSION_FLUVIAL_GES_DIESEL = 3.17  # kg CO2e/L de diesel

# Facteurs d'émission routier (ADEME)
FACTEUR_EMISSION_CAMION_ARTICULE = 0.0993  # kgCO2e/t.km
# Conditions ADEME : Camion articulé <34t, taux de charge 60%, retour à vide 17%
# Note : Pour pré/post-acheminement optimisés (100% charge), marge d'incertitude de -30%
