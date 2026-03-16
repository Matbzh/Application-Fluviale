# Chargement des librairies
import os
import pandas as pd
import math as math
from Fluvial_data.registry import REGISTRY
from Fluvial_data.barges import Automoteur_Caracteristiques, Pousseur_Caracteristiques
from Fluvial_data.camions import Camion_Caracteristiques
from Fluvial_data.parametres import *

# Chargement du répertoire de travail
os.chdir("/Users/mathieu/Documents/Application Fluviale")

# ======= Calcul des variables du transport fluvial =======

## ======= Définition des variables =======
### Description des marchandises
Volume_transporte = float()
### Itinéraire
Sens_circulation = str()
Distance = float()
Voie_deau = str()
### Description de l'embarcation
Type_Embarcation = str()
Volume_Embarcation = float()

## ====== Recherche des données pertinentes =======

### ====== Travailler en tonne.kilomètres ======
Volume_transporte = 120000
Volume_Embarcation = 1150
Distance = 49

Nombre_de_trajets = math.ceil(Volume_transporte/Volume_Embarcation)
Nombre_de_trajets

Taux_remplissage = Volume_transporte/(Volume_Embarcation*Nombre_de_trajets) # pour information
Taux_remplissage # pour information

Tonne_km = Nombre_de_trajets*Volume_Embarcation*Distance # Hypothèse : chaque barge est pleine.
Tonne_km


### ====== Fonction de normalisation des libellés des types d'embarcation ======
def reduc_lib_type_embarcation(Type_Embarcation):
    if Type_Embarcation.lower() == "automoteur":
        Type_Embarcation_court = "Atm"
    elif Type_Embarcation.lower() == "pousseur":
        Type_Embarcation_court = "Psr"
    else:
        raise ValueError("Type_embarcation doit être 'Automoteur' ou 'Pousseur'")
    return Type_Embarcation_court

#### Simulation
Type_Embarcation = "Pousseur"
reduc_lib_type_embarcation(Type_Embarcation) # ça fonctionne


### ===== Fonction de construction des titres pour rechercher le dataframe pertinent =====
def Conso_dftitle_building(Type_Embarcation, Voie_deau):
    Titre = ("Conso",reduc_lib_type_embarcation(Type_Embarcation), Voie_deau, "Standard")
    Titre2 = "_".join(Titre)
    Titre2 = Titre2.strip('"').strip("'")
    return Titre2

#### Simulation
Consommation_Embarcation_Voiedeau = REGISTRY[Conso_dftitle_building("Automoteur","Seine")]
Consommation_Embarcation_Voiedeau


### ===== Fonction de recherche de la valeur pertinente =====
def choix_valeur_conso(Volume_Embarcation, Sens_circulation):
    Ligne_pertinente = Consommation_Embarcation_Voiedeau[
        (Consommation_Embarcation_Voiedeau["Capacité min"] <= Volume_Embarcation) &
        (Consommation_Embarcation_Voiedeau["Capacité max"] >= Volume_Embarcation)
    ]
    if Sens_circulation == "Montant":
        Sens_circulation_long = "Montant_Compute"
    elif Sens_circulation == "Avalant":
        Sens_circulation_long = "Avalant_Compute"
    else: Sens_circulation_long = "Mixte_Compute"
    valeur_finale = Ligne_pertinente[Sens_circulation_long]
    return valeur_finale

#### Simulation
choix_valeur_conso(Volume_Embarcation = 1300, Sens_circulation = "Mixte") # ça fonctionne

## ===== Calcul de la consommation et des émissions fluviales =====
### Extraction de la valeur de consomamtion du tableau 
Valeur_conso = choix_valeur_conso(
    Volume_Embarcation = 1300,
    Sens_circulation = "Mixte"
).values[0]
Valeur_conso

### Consommation totale en litres
Consommation_totale_L = Valeur_conso*Tonne_km
Consommation_totale_L

### Emissions totales en gCO2
Emissions_Total_kgCO2 = Consommation_totale_L * FACTEUR_EMISSION_FLUVIAL_CO2_DIESEL
Emissions_Total_tCO2 = Emissions_Total_kgCO2/1000 
Emissions_Total_tCO2

### Emissions totales en gCO2e
Emissions_Total_kgCO2e = Consommation_totale_L * FACTEUR_EMISSION_FLUVIAL_GES_DIESEL
Emissions_Total_tCO2e = Emissions_Total_kgCO2e/1000

### Affichage des résultats
print(f"Consommation fluviale totale: {Consommation_totale_L:,.0f}" .replace(","," ") + " Litres")
print(f"Emissions fluviale de CO2 : {Emissions_Total_tCO2:.0f} Tonnes")
print(f"Emissions fluviale de CO2e : {Emissions_Total_tCO2e:.0f} Tonnes")

# ===== Calcul des émissions routières =====
## ===== Définition des variables =====
Distance_routière = float()
Distance_routière = 49
## ===== Calcul du nombre de tonnes.km =====
Tkm_Routières = Volume_transporte * Distance_routière
## ===== Calcul des émissions =====
Emissions_routières_Kg = Tkm_Routières * FACTEUR_EMISSION_CAMION_ARTICULE
Emissions_routières_T = Emissions_routières_Kg/1000
## ===== Affichage des résultats =====
print(f"Emissions routière de CO2 : {Emissions_routières_T:.0f} Tonnes")

