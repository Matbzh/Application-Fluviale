# calculs.py
import math
from Fluvial_data.registry import REGISTRY
from Fluvial_data.parametres import (
    FACTEUR_EMISSION_FLUVIAL_CO2_DIESEL,
    FACTEUR_EMISSION_FLUVIAL_GES_DIESEL,
    FACTEUR_EMISSION_CAMION_ARTICULE
)

# Formulation de la fonction du calcul des émissions de transport fluvial
def calcul_fluvial(volume_transporte, volume_embarcation, distance, type_embarcation, voie_deau, sens_circulation):
    
    # Étape 1 : calcul des tonne.km
    nombre_de_trajets = math.ceil(volume_transporte / volume_embarcation)
    tonne_km = nombre_de_trajets * volume_embarcation * distance

    # Étape 2 : trouver le bon tableau de consommation
    def reduc_lib(type_embarcation):
        if type_embarcation.lower() == "automoteur":
            return "Atm"
        elif type_embarcation.lower() == "pousseur":
            return "Psr"
        else:
            raise ValueError("Type d'embarcation invalide")

    titre = "Conso_" + reduc_lib(type_embarcation) + "_" + voie_deau + "_Standard"
    df_conso = REGISTRY[titre]

    # Étape 3 : trouver la valeur de consommation
    ligne = df_conso[
        (df_conso.iloc[:, 0] <= volume_embarcation) &
        (df_conso.iloc[:, 1] >= volume_embarcation)
    ]
    if sens_circulation == "Montant":
        colonne = "Montant_Compute"
    elif sens_circulation == "Avalant":
        colonne = "Avalant_Compute"
    else:
        colonne = "Mixte_Compute"
    valeur_conso = ligne[colonne].values[0]

    # Étape 4 : calcul des émissions
    consommation_L = tonne_km * valeur_conso
    emissions_co2_t = (consommation_L * FACTEUR_EMISSION_FLUVIAL_CO2_DIESEL) / 1000
    emissions_ges_t = (consommation_L * FACTEUR_EMISSION_FLUVIAL_GES_DIESEL) / 1000

    return {
        "tonne_km": tonne_km,
        "consommation_L": consommation_L,
        "emissions_co2_t": emissions_co2_t,
        "emissions_ges_t": emissions_ges_t
    }


# Formulation de la fonction du calcul des émissions de transport routier
def calcul_routier(volume_transporte, distance_routiere):
    
    # Calcul des tonne.km
    tonne_km = volume_transporte * distance_routiere
    
    # Calcul des émissions
    emissions_ges_kg = tonne_km * FACTEUR_EMISSION_CAMION_ARTICULE
    emissions_ges_t = emissions_ges_kg / 1000

    return {
        "tonne_km": tonne_km,
        "emissions_ges_t": emissions_ges_t
    }
