# ===== Les tableaux des consommations =====
## 1. Les imports
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

## 2. Le dictionnaire (à ajouter en dessous)
REGISTRY = {
    "Conso_Atm_Seine_Standard": Conso_Atm_Seine_Standard,
    "Conso_Atm_PetiteSeine_Oise_Standard": Conso_Atm_PetiteSeine_Oise_Standard,
    "Conso_Atm_Rhone_Saone_Standard": Conso_Atm_Rhone_Saone_Standard,
    "Conso_Atm_Rhin_Standard": Conso_Atm_Rhin_Standard,
    "Conso_Atm_Moselle_Standard": Conso_Atm_Moselle_Standard,
    "Conso_Atm_Canal_Standard": Conso_Atm_Canal_Standard,
    "Conso_Psr_Seine_Standard": Conso_Psr_Seine_Standard,
    "Conso_Psr_PetiteSeine_Oise_Standard": Conso_Psr_PetiteSeine_Oise_Standard,
    "Conso_Psr_Rhone_Saone_Standard": Conso_Psr_Rhone_Saone_Standard,
    "Conso_Psr_Rhin_Standard": Conso_Psr_Rhin_Standard,
    "Conso_Psr_Moselle_Standard": Conso_Psr_Moselle_Standard,
    "Conso_Psr_Canal_Standard": Conso_Psr_Canal_Standard
}

