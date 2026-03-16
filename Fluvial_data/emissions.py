# Chargement des librairies
import pandas as pd
from .fonctions_base import tableau_embarcation, tableau_embarcation_canal

## Environnement
### Émissions des automoteurs, en gCO2/t.km, 31% de vide ----
#### Seine ----
R_400 = [0, 400, 52.9, 51.7, 52.3]
R_649 = [400, 649, 44.9, 44, 44.4]
R_999 = [650, 999, 30.8, 30.1, 30.5]
R_1499 = [1000, 1499, 17.8, 17.4, 17.6]
R_3000 = [1500, 3000, 16.4, 9.5, 12.9]
R_9000 = [3000, 9000, 10, 5.8, 7.8]

Emission_Atm_Seine_Vide_31 = tableau_embarcation("Automoteur",
                                                 R_400,R_649,R_999,R_1499,R_3000,R_9000)
Emission_Atm_Seine_Vide_31

#### Petite Seine / Oise ----
R_400 = [0, 400, 40.6, 38.7, 39.6]
R_649 = [400, 649, 42.2, 38.5, 40.3]
R_999 = [650, 999, 21.1, 19.5, 20.3]
R_1499 = [1000, 1499, 14.9, 14.0, 14.5]
R_3000 = [1500, 3000, 18.3, 10.2, 14.2]
R_9000 = [3000, 9000, None, None, None]

Emission_Atm_PetiteSeine_Oise_Vide_31 = tableau_embarcation("Automoteur",
                                                            R_400,R_649,R_999,R_1499,R_3000,R_9000)
Emission_Atm_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_400 = [0, 400, 61.2, 49.5, 55.9]
R_649 = [400, 649, 52.3, 38.7, 45.9]
R_999 = [650, 999, 35.9, 27.5, 31.5]
R_1499 = [1000, 1499, 28.5, 21.4, 25.2]
R_3000 = [1500, 3000, 26.3, 18.7, 22.5]
R_9000 = [3000, 9000, 16, 12, 14]

Emission_Atm_Rhone_Saone_Vide_31 = tableau_embarcation("Automoteur",
                                                       R_400,R_649,R_999,R_1499,R_3000,R_9000)
Emission_Atm_Rhone_Saone_Vide_31

#### Rhin ----
R_400 = [0, 400, None,None,None]
R_649 = [400, 649, None,None,None]
R_999 = [650, 999, None,None,None]
R_1499 = [1000, 1499, 47.4, 15.5, 33.3]
R_3000 = [1500, 3000, 29.3, 9.6, 20.6]
R_9000 = [3000, 9000, 17.9, 5.8, 12.5]

Emission_Atm_Rhin_Vide_31 = tableau_embarcation("Automoteur",
                                                R_400,R_649,R_999,R_1499,R_3000,R_9000)
Emission_Atm_Rhin_Vide_31

#### Moselle ----
R_400 = [0, 400, 63.1, 51, 57]
R_649 = [400, 649, 53.9, 39.9, 46.7]
R_999 = [650, 999, 36.9, 27.3,32]
R_1499 = [1000, 1499, 29.4, 22, 25.6]
R_3000 = [1500, 3000, 18.2, 13.6, 15.9]
R_9000 = [3000, 9000, 17.9, 5.8, 11.6]

Emission_Atm_Moselle_Vide_31 = tableau_embarcation("Automoteur",
                                                   R_400,R_649,R_999,R_1499,R_3000,R_9000)
Emission_Atm_Moselle_Vide_31

#### Canal ----
##### Canal Grand Gabarit
R_400 = [0, 400, None]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, 43.2]
R_3000 = [1500, 3000, 26.9]
R_9000 = [3000, 9000, 26.9]

Canal_GG = tableau_embarcation_canal("automoteur", "Canal GG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_GG

##### Canal Moyen Gabarit
R_400 = [0, 400, 32.9]
R_649 = [400, 649, 31.3]
R_999 = [650, 999, 29.7]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 3000, None]
R_9000 = [3000, 9000, None]

Canal_MG = tableau_embarcation_canal("automoteur", "Canal MG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_MG

##### Canal Petit Gabarit
R_400 = [0, 400, 26.6]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 3000, None]
R_9000 = [3000, 9000, None]

Canal_PG = tableau_embarcation_canal("automoteur", "Canal PG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_PG

##### Canal consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Capacité min","Capacité max"], how="left")
Emission_Atm_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Capacité min","Capacité max"], how="left")
Emission_Atm_Canal_Vide_31

### Émissions des pousseurs, en gCO2/t.km, 31% de vide ----
#### Seine ----
R_880 = [0,880, 38.8, 27.7, 33.2]
R_881 = [881,10000, 10.4, 5.2, 7.7]
Emission_Psr_Seine_Vide_31 = tableau_embarcation("pousseur",R_880,R_881)
Emission_Psr_Seine_Vide_31

#### Petite Seine / Oise ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, None, None, None]
Emission_Psr_PetiteSeine_Oise_Vide_31 = tableau_embarcation("pousseur",R_880,R_881)
Emission_Psr_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_880 = [0,880, 40.2, 26.6, 33.4]
R_881 = [881,10000, 11.8, 7.2, 9.5]
Emission_Psr_Rhone_Saone_Vide_31 = tableau_embarcation("pousseur",R_880,R_881)
Emission_Psr_Rhone_Saone_Vide_31

#### Rhin ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, 11.8, 7.2, 9.5]
Emission_Psr_Rhin_Vide_31 = tableau_embarcation("pousseur",R_880,R_881)
Emission_Psr_Rhin_Vide_31

#### Moselle ----
R_880 = [0,880,  None, None, None]
R_881 = [881,10000, 11.8, 7.2, 9.5]
Emission_Psr_Moselle_Vide_31 = tableau_embarcation("pousseur",R_880,R_881)
Emission_Psr_Moselle_Vide_31

#### Canal ----
##### Canal Grand Gabarit
R_880 = [0,880, None]
R_881 = [881,10000, 9.9]
Canal_GG = tableau_embarcation_canal("pousseur","Canal GG",R_880,R_881)

##### Canal Moyen Gabarit
R_880 = [0,880, 20.6]
R_881 = [881,10000, None]
Canal_MG = tableau_embarcation_canal("pousseur","Canal MG",R_880,R_881)

##### Canal Petit Gabarit
R_880 = [0,880, None]
R_881 = [881,10000, None]
Canal_PG = tableau_embarcation_canal("pousseur","Canal PG",R_880,R_881)

##### Canal Consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Puissance min","Puissance max"], how="left")
Emission_Psr_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Puissance min","Puissance max"], how="left")
Emission_Psr_Canal_Vide_31

### Émissions des automoteurs, en gCO2e/t.km, 31% de vide ----
#### Seine ----
R_400 = [0, 400, 54.6, 53.4, 54]
R_649 = [400, 649, 46.4, 45.4, 45.9]
R_999 = [650, 999, 31.8, 31.1, 31.5]
R_1499 = [1000, 1499, 18.3, 17.9, 18.1]
R_3000 = [1500, 3000, 16.9, 9.8, 13.3]
R_9000 = [3000, 9000, 10.3, 6, 8.1]

EmissionGES_Atm_Seine_Vide_31 = tableau_embarcation("Automoteur",
                                                    R_400,R_649,R_999,R_1499,R_3000,R_9000)
EmissionGES_Atm_Seine_Vide_31

#### Petite Seine / Oise ----
R_400 = [0, 400, 42, 39.9, 40.9]
R_649 = [400, 649, 43.6, 39.8, 41.6]
R_999 = [650, 999, 21.8, 20.1, 20.9]
R_1499 = [1000, 1499, 15.4, 14.5, 14.9]
R_3000 = [1500, 3000, 18.9, 10.5, 14.6]
R_9000 = [3000, 9000, None, None, None]

EmissionGES_Atm_PetiteSeine_Oise_Vide_31 = tableau_embarcation("Automoteur",
                                                               R_400,R_649,R_999,R_1499,R_3000,R_9000)
EmissionGES_Atm_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_400 = [0, 400, 63.2, 51.1, 57.8]
R_649 = [400, 649, 54, 40, 47.4]
R_999 = [650, 999, 37, 27.4, 32.5]
R_1499 = [1000, 1499, 29.4, 22.1, 26]
R_3000 = [1500, 3000, 27.1, 19.3, 23.3]
R_9000 = [3000, 9000, 16.5, 12.4, 14.5]

EmissionGES_Atm_Rhone_Saone_Vide_31 = tableau_embarcation("Automoteur",
                                                          R_400,R_649,R_999,R_1499,R_3000,R_9000)
EmissionGES_Atm_Rhone_Saone_Vide_31

#### Rhin ----
R_400 = [0, 400, None,None,None]
R_649 = [400, 649, None,None,None]
R_999 = [650, 999, None,None,None]
R_1499 = [1000, 1499, 48.9, 16, 34.4]
R_3000 = [1500, 3000, 30.3, 9.9, 21.3]
R_9000 = [3000, 9000, 18.4, 6, 13]

EmissionGES_Atm_Rhin_Vide_31 = tableau_embarcation("Automoteur",
                                                   R_400,R_649,R_999,R_1499,R_3000,R_9000)
EmissionGES_Atm_Rhin_Vide_31

#### Moselle ----
R_400 = [0, 400, 65.1, 52.7, 58.9]
R_649 = [400, 649, 55.6, 41.2, 48.2]
R_999 = [650, 999, 38.1, 28.2,33.1]
R_1499 = [1000, 1499, 30.3, 22.8, 26.5]
R_3000 = [1500, 3000, 18.8, 14.1, 16.4]
R_9000 = [3000, 9000, 18.4, 6, 11.9]

EmissionGES_Atm_Moselle_Vide_31 = tableau_embarcation("Automoteur",
                                                      R_400,R_649,R_999,R_1499,R_3000,R_9000)
EmissionGES_Atm_Moselle_Vide_31

#### Canal
##### Canal Grand Gabarit 
R_400 = [0, 400, None]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, 44.7]
R_3000 = [1500, 3000, 27.8]
R_9000 = [3000, 9000, 27.8]

Canal_GG = tableau_embarcation_canal("automoteur","Canal GG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)

##### Canal Moyen Gabarit 
R_400 = [0, 400, 34]
R_649 = [400, 649, 32.3]
R_999 = [650, 999, 30.7]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 3000, None]
R_9000 = [3000, 9000, None]

Canal_MG = tableau_embarcation_canal("automoteur","Canal MG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)

##### Canal Petit Gabarit
R_400 = [0, 400, 27.5]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 3000, None]
R_9000 = [3000, 9000, None]

Canal_PG = tableau_embarcation_canal("automoteur","Canal PG",
                                     R_400,R_649,R_999,R_1499,R_3000,R_9000)

##### Canal Consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Capacité min","Capacité max"], how="left")
EmissionGES_Atm_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Capacité min","Capacité max"], how="left")
EmissionGES_Atm_Canal_Vide_31

### Émissions des pousseurs, en gCO2e/t.km, 31% de vide ----
#### Seine ----
R_880 = [0,880, 40.1, 28.6, 34.3]
R_881 = [881,10000, 10.7, 5.4, 8]
EmissionGES_Psr_Seine_Vide_31 = tableau_embarcation("Pousseur",R_880,R_881)
EmissionGES_Psr_Seine_Vide_31

#### Petite Seine / Oise ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, None, None, None]
EmissionGES_Psr_PetiteSeine_Oise_Vide_31 = tableau_embarcation("Pousseur",R_880,R_881)
EmissionGES_Psr_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_880 = [0,880, 41.5, 27.4, 34.5]
R_881 = [881,10000, 12.2, 7.5, 9.8]
EmissionGES_Psr_Rhone_Saone_Vide_31 = tableau_embarcation("Pousseur",R_880,R_881)
EmissionGES_Psr_Rhone_Saone_Vide_31

#### Rhin ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, 12.2, 7.5, 10.1]
EmissionGES_Psr_Rhin_Vide_31 = tableau_embarcation("Pousseur",R_880,R_881)
EmissionGES_Psr_Rhin_Vide_31

#### Moselle ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, 12.2, 7.5, 9.8]
EmissionGES_Psr_Moselle_Vide_31 = tableau_embarcation("Pousseur",R_880,R_881)
EmissionGES_Psr_Moselle_Vide_31

#### Canal
##### Canal Grand Gabarit
R_880 = [0,880, None]
R_881 = [881,10000, 10.2]
Canal_GG = tableau_embarcation_canal("Pousseur","Canal GG",R_880,R_881)
Canal_GG

##### Canal Moyen Gabarit
R_880 = [0,880, 21.3]
R_881 = [881,10000, None]
Canal_MG = tableau_embarcation_canal("Pousseur","Canal MG",R_880,R_881)
Canal_MG

##### Canal Moyen Gabarit
R_880 = [0,880, None]
R_881 = [881,10000, None]
Canal_PG = tableau_embarcation_canal("Pousseur","Canal PG",R_880,R_881)
Canal_PG

##### Canal Consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Puissance min","Puissance max"], how="left")
EmissionGES_Psr_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Puissance min","Puissance max"], how="left")
EmissionGES_Psr_Canal_Vide_31

# Emissions calculées
## Fonction de calcul des émissions de CO2 (3.07kg/L) et des émissions GES (3.17 kg/L)
def emission_standardisee(df, type_emission):
    # Définir le facteur selon le type d'émission
    if type_emission.upper() == "CO2":
        facteur = 3.07 * 1000
    elif type_emission.upper() == "GES":
        facteur = 3.17 * 1000
    else:
        raise ValueError("type_emission doit être 'CO2' ou 'GES'")
    # Isoler les deux premières colonnes (Capacité min/max ou Puissance min/max)
    colonnes_fixes = df.iloc[:, :2]
    # Multiplier les colonnes suivantes par le facteur
    colonnes_calculees = df.iloc[:, 2:] * facteur
    # Recomposer le DataFrame final
    return pd.concat([colonnes_fixes, colonnes_calculees], axis=1)