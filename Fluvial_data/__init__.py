"""
Package de données fluviales
"""
from .fonctions_base import tableau_embarcation, tableau_embarcation_canal
from .consommations import (
    Conso_Atm_Seine_Standard,
    Conso_Atm_PetiteSeine_Oise_Standard,
    Conso_Atm_Rhone_Saone_Standard,
    Conso_Atm_Rhin_Standard,
    Conso_Atm_Moselle_Standard,
    Conso_Atm_Canal_Standard,
    Conso_Psr_Seine_Standard,
    Conso_Psr_PetiteSeine_Oise_Standard,
    Conso_Psr_Rhone_Saone_Standard,
    Conso_Psr_Rhin_Standard,
    Conso_Psr_Moselle_Standard,
    Conso_Psr_Canal_Standard
)
from .emissions import *
from .registry import REGISTRY
from .barges import Automoteur_Caracteristiques, Pousseur_Caracteristiques
from .camions import Camion_Caracteristiques
from .parametres import (
    VITESSE_PRE_POST_ACHEMINEMENT, 
    FACTEUR_EMISSION_FLUVIAL_CO2_DIESEL, 
    FACTEUR_EMISSION_FLUVIAL_GES_DIESEL,
    FACTEUR_EMISSION_CAMION_ARTICULE)