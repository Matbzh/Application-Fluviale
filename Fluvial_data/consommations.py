# Chargement des librairies
import pandas as pd
from .fonctions_base import tableau_embarcation, tableau_embarcation_canal

### Automoteurs, en L/t.km, hors vide ----
#### Seine ----
R_400 = [0, 400, 0.014, 0.014, 0.014]
R_649 = [400, 649, 0.012, 0.012, 0.012]
R_999 = [650, 999, 0.008, 0.008, 0.008]
R_1499 = [1000, 1499, 0.005, 0.005, 0.005]
R_3000 = [1500, 2999, 0.004, 0.002, 0.003]
R_9000 = [3000, 9000, 0.003, 0.002, 0.002]

Conso_Atm_Seine_Hors_Vide = tableau_embarcation("Automoteur", R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Seine_Hors_Vide

#### Petite Seine / Oise ----
R_400 = [0, 400, 0.010, 0.010, 0.010]
R_649 = [400, 649, 0.010, 0.010, 0.010]
R_999 = [650, 999, 0.005, 0.005, 0.005]
R_1499 = [1000, 1499, 0.003, 0.003, 0.003]
R_3000 = [1500, 2999, 0.005, 0.002, 0.004]
R_9000 = [3000, 9000, None, None, None]

Conso_Atm_PetiteSeine_Oise_Hors_Vide = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_PetiteSeine_Oise_Hors_Vide

#### Rhône Saône ----
R_400 = [0, 400, 0.015, 0.013, 0.014]
R_649 = [400, 649, 0.013, 0.010, 0.012]
R_999 = [650, 999, 0.009, 0.007, 0.008]
R_1499 = [1000, 1499, 0.007, 0.005, 0.006]
R_3000 = [1500, 2999, 0.007, 0.005, 0.006]
R_9000 = [3000, 9000, 0.004, 0.003, 0.004]

Conso_Atm_Rhone_Saone_Hors_Vide = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Rhone_Saone_Hors_Vide

#### Rhin ----
R_400 = [0, 400, None, None, None]
R_649 = [400, 649, None, None, None]
R_999 = [650, 999, None, None, None]
R_1499 = [1000, 1499, 0.012, 0.004, 0.008]
R_3000 = [1500, 2999, 0.007, 0.003, 0.005]
R_9000 = [3000, 9000, 0.004, 0.002, 0.003]

Conso_Atm_Rhin_Hors_Vide = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Rhin_Hors_Vide

#### Moselle ----
R_400 = [0, 400, 0.016, 0.014, 0.015]
R_649 = [400, 649, 0.013, 0.011, 0.012]
R_999 = [650, 999, 0.009, 0.007, 0.008]
R_1499 = [1000, 1499, 0.007, 0.006, 0.007]
R_3000 = [1500, 2999, 0.004, 0.004, 0.004]
R_9000 = [3000, 9000, 0.004, 0.002, 0.003]

Conso_Atm_Moselle_Hors_Vide = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Moselle_Hors_Vide

#### Canal
##### Canal Grand Gabarit
Canal_GG = tableau_embarcation_canal("Automoteur","Canal GG",
    [0, 400, None],
    [400, 649, None],
    [650, 999, None],
    [1000, 1499, 0.010],
    [1500, 2999, 0.006],
    [3000, 9000, 0.006]
)
Canal_GG

##### Canal Moyen Gabarit
Canal_MG = tableau_embarcation_canal("Automoteur","Canal MG",
    [0, 400, 0.008],
    [400, 649, 0.008],
    [650, 999, 0.007],
    [1000, 1499, None],
    [1500, 2999, None],
    [3000, 9000, None]
)
Canal_MG

##### Canal Petit Gabarit
Canal_PG = tableau_embarcation_canal("Automoteur","Canal PG",
    [0, 400, 0.006],
    [400, 649, None],
    [650, 999, None],
    [1000, 1499, None],
    [1500, 2999, None],
    [3000, 9000, None]
)
Canal_PG

##### Canal consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Capacité min","Capacité max"], how="left")
Conso_Atm_Canal_Hors_Vide = Canal_Conso.merge(Canal_PG, on=["Capacité min","Capacité max"], how="left")
Conso_Atm_Canal_Hors_Vide

### Pousseur, en L/t.km, hors vide ----
#### Puissance en kW, 880 kW correspond à ~1200 CV, pour une capacité de poussage de ~2200 tonnes
#### Seine ----
R_880 = [0,800, 0.009, 0.007, 0.008]
R_881 = [801,10000, 0.003, 0.001, 0.002]

Conso_Psr_Seine_Hors_Vide = tableau_embarcation("Pousseur",R_880, R_881)
Conso_Psr_Seine_Hors_Vide

#### Petite Seine / Oise ----
R_880 = [0,800, None, None, None]
R_881 = [801,10000, None, None, None]

Conso_Psr_PetiteSeine_Oise_Hors_Vide = tableau_embarcation("Pousseur",R_880, R_881)
Conso_Psr_PetiteSeine_Oise_Hors_Vide

#### Rhône Saône ----
R_880 = [0,800, 0.010, 0.007, 0.009]
R_881 = [801,10000, 0.003, 0.002, 0.002]

Conso_Psr_Rhone_Saone_Hors_Vide = tableau_embarcation("Pousseur",R_880, R_881)
Conso_Psr_Rhone_Saone_Hors_Vide

#### Rhin ----
R_880 = [0,800, None , None, None]
R_881 = [801,10000, 0.003, 0.002, 0.002]

Conso_Psr_Rhin_Hors_Vide = tableau_embarcation("Pousseur",R_880, R_881)
Conso_Psr_Rhin_Hors_Vide

#### Moselle ----
R_880 = [0,800, None,None,None]
R_881 = [801,10000, 0.003, 0.002, 0.002]

Conso_Psr_Moselle_Hors_Vide = tableau_embarcation("Pousseur",R_880, R_881)
Conso_Psr_Moselle_Hors_Vide

#### Canal ----
##### Canal Grand Gabarit
Canal_GG = tableau_embarcation_canal("Pousseur","Canal GG",
    [0,800,None],
    [801,10000,0.002])
Canal_GG

##### Canal Moyen Gabarit
Canal_MG = tableau_embarcation_canal("Pousseur","Canal MG",
    [0,800,0.005],
    [801,10000,None])
Canal_MG

##### Canal Moyen Gabarit
Canal_PG = tableau_embarcation_canal("Pousseur","Canal PG",
    [0,800,None],
    [801,10000,None])
Canal_PG

##### Canal consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Puissance min","Puissance max"], how="left")
Conso_Psr_Canal_Hors_Vide = Canal_Conso.merge(Canal_PG, on=["Puissance min","Puissance max"], how="left")
Conso_Psr_Canal_Hors_Vide

### Automoteurs, en L/t.km, 31% de vide ----
#### Seine ----
R_400 = [0, 400, 0.017, 0.017, 0.017]
R_649 = [400, 649, 0.015, 0.014, 0.014]
R_999 = [650, 999, 0.010, 0.010, 0.010]
R_1499 = [1000, 1499, 0.006, 0.006, 0.006]
R_3000 = [1500, 2999, 0.005, 0.003, 0.004]
R_9000 = [3000, 9000, 0.003, 0.002, 0.003]

Conso_Atm_Seine_Vide_31 = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Seine_Vide_31

#### Petite Seine / Oise ----
R_400 = [0, 400, 0.013, 0.013, 0.013]
R_649 = [400, 649, 0.014, 0.013, 0.013]
R_999 = [650, 999, 0.007, 0.006, 0.007]
R_1499 = [1000, 1499, 0.005, 0.005, 0.005]
R_3000 = [1500, 2999, 0.006, 0.003, 0.005]
R_9000 = [3000, 9000, None, None, None]

Conso_Atm_PetiteSeine_Oise_Vide_31 = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_400 = [0, 400, 0.02, 0.016, 0.018]
R_649 = [400, 649, 0.017, 0.013, 0.015]
R_999 = [650, 999, 0.012, 0.009, 0.010]
R_1499 = [1000, 1499, 0.009, 0.007, 0.008]
R_3000 = [1500, 2999, 0.009, 0.006, 0.007]
R_9000 = [3000, 9000, 0.005, 0.004, 0.005]

Conso_Atm_Rhone_Saone_Vide_31 = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Rhone_Saone_Vide_31

#### Rhin ----
R_400 = [0, 400, None, None, None]
R_649 = [400, 649, None, None, None]
R_999 = [650, 999, None, None, None]
R_1499 = [1000, 1499, 0.015, 0.005, 0.011]
R_3000 = [1500, 2999, 0.010, 0.003, 0.007]
R_9000 = [3000, 9000, 0.006, 0.002, 0.004]

Conso_Atm_Rhin_Vide_31 = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Rhin_Vide_31

#### Moselle ----
R_400 = [0, 400, 0.021, 0.017, 0.019]
R_649 = [400, 649, 0.018, 0.013, 0.015]
R_999 = [650, 999, 0.012, 0.009, 0.010]
R_1499 = [1000, 1499, 0.010, 0.007, 0.008]
R_3000 = [1500, 2999, 0.006, 0.004, 0.005]
R_9000 = [3000, 9000, 0.004, 0.002, 0.004]

Conso_Atm_Moselle_Vide_31 = tableau_embarcation("Automoteur",R_400,R_649,R_999,R_1499,R_3000,R_9000)
Conso_Atm_Moselle_Vide_31

#### Canal ----
#### Canal Grand Gabarit ----
R_400 = [0, 400, None]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, 0.014]
R_3000 = [1500, 2999, 0.009]
R_9000 = [3000, 9000, 0.009]

Canal_GG = tableau_embarcation_canal("Automoteur", "Canal GG", R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_GG

#### Canal Moyen Gabarit ----
R_400 = [0, 400, 0.011]
R_649 = [400, 649, 0.010]
R_999 = [650, 999, 0.010]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 2999, None]
R_9000 = [3000, 9000, None]

Canal_MG = tableau_embarcation_canal("Automoteur", "Canal MG", R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_MG

#### Canal Petit Gabarit ----
R_400 = [0, 400, 0.009]
R_649 = [400, 649, None]
R_999 = [650, 999, None]
R_1499 = [1000, 1499, None]
R_3000 = [1500, 2999, None]
R_9000 = [3000, 9000, None]

Canal_PG = tableau_embarcation_canal("Automoteur", "Canal PG", R_400,R_649,R_999,R_1499,R_3000,R_9000)
Canal_PG

##### Canal consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Capacité min","Capacité max"], how="left")
Conso_Atm_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Capacité min","Capacité max"], how="left")
Conso_Atm_Canal_Vide_31

### Pousseurs, en L/t.km, 31% de vide ----
#### Puissance en kW, 880 kW correspond à ~1200 CV, pour une capacité de poussage de ~2200 tonnes
#### Seine ----
R_880 = [0,880, 0.013, 0.009, 0.011]
R_881 = [881,10000, 0.003, 0.002, 0.003]

Conso_Psr_Seine_Vide_31 = tableau_embarcation("Pousseur", R_880, R_881)
Conso_Psr_Seine_Vide_31

#### Petite Seine / Oise ----
R_880 = [0,880, None, None, None]
R_881 = [881,10000, None, None, None]

Conso_Psr_PetiteSeine_Oise_Vide_31 = tableau_embarcation("Pousseur", R_880, R_881)
Conso_Psr_PetiteSeine_Oise_Vide_31

#### Rhône Saône ----
R_880 = [0,880, 0.013, 0.009, 0.011]
R_881 = [881,10000, 0.004, 0.002, 0.003]

Conso_Psr_Rhone_Saone_Vide_31 = tableau_embarcation("Pousseur", R_880, R_881)
Conso_Psr_Rhone_Saone_Vide_31

#### Rhin ----
R_880 = [0,880, None, None, None]
R_881 = [881, 10000, 0.004, 0.002, 0.003]

Conso_Psr_Rhin_Vide_31 = tableau_embarcation("Pousseur", R_880, R_881)
Conso_Psr_Rhin_Vide_31

#### Moselle ----
R_880 = [0,880, None, None, None]
R_881 = [881, 10000, 0.004, 0.002, 0.003]

Conso_Psr_Moselle_Vide_31 = tableau_embarcation("Pousseur", R_880, R_881)
Conso_Psr_Moselle_Vide_31

#### Canal ----
##### Canal Grand Gabarit
R_880 = [0, 880, None]
R_881 = [881, 10000, 0.003]

Canal_GG = tableau_embarcation_canal("Pousseur", "Canal GG", R_880, R_881)
Canal_GG

##### Canal Moyen Gabarit
R_880 = [0, 880, 0.007]
R_881 = [881, 10000, None]

Canal_MG = tableau_embarcation_canal("Pousseur", "Canal MG", R_880, R_881)
Canal_MG

##### Canal Petit Gabarit
R_880 = [0, 880, None]
R_881 = [881, 10000, None]

Canal_PG = tableau_embarcation_canal("Pousseur", "Canal PG", R_880, R_881)
Canal_PG

##### Canal consolidé
Canal_Conso = Canal_GG.merge(Canal_MG, on=["Puissance min","Puissance max"], how="left")
Conso_Psr_Canal_Vide_31 = Canal_Conso.merge(Canal_PG, on=["Puissance min","Puissance max"], how="left")
Conso_Psr_Canal_Vide_31


### Consommation standardisée des Automoteurs, en L/t.km ----
#### Fonction pour créer les tableaux standardisées des Automoteurs
def conso_atm_standard(Conso_Vide31, Conso_HorsVide):
    # Concaténation des datasets
    df = pd.concat([Conso_Vide31.reset_index(drop=True),
                    Conso_HorsVide.reset_index(drop=True)],
                    axis=1)
    # Renommage des colonnes
    df.columns = ["Capacité min Vide31", "Capacité max Vide31",
                  "Montant_Vide31", "Avalant_Vide31", "Mixte_Vide31",
                  "Capacité min HorsVide", "Capacité max HorsVide",
                  "Montant_HorsVide","Avalant_HorsVide","Mixte_HorsVide"]
    # Calcul des moyennes
    df["Montant_Compute"] = (df["Montant_Vide31"]/1.31 + df["Montant_HorsVide"])/2
    df["Avalant_Compute"] = (df["Avalant_Vide31"]/1.31 + df["Avalant_HorsVide"])/2
    df["Mixte_Compute"] = (df["Mixte_Vide31"]/1.31 + df["Mixte_HorsVide"])/2
    # Sélection des colonnes finales
    return df[["Capacité min HorsVide", "Capacité max HorsVide", "Montant_Compute", "Avalant_Compute", "Mixte_Compute"]].rename(columns={
        "Capacité min HorsVide": "Capacité min", 
        "Capacité max HorsVide": "Capacité max"
    })



#### Fonction pour créer les tableaux standardisées des Pousseurs
def conso_psr_standard(Conso_Vide31, Conso_HorsVide):
    # Concaténation des datasets
    df = pd.concat([Conso_Vide31.reset_index(drop=True),
                    Conso_HorsVide.reset_index(drop=True)],
                    axis=1)
    # Renommage des colonnes
    df.columns = ["Puissance min Vide31", "Puissance max Vide31",
                  "Montant_Vide31", "Avalant_Vide31", "Mixte_Vide31",
                  "Puissance min HorsVide", "Puissance max HorsVide",
                  "Montant_HorsVide","Avalant_HorsVide","Mixte_HorsVide"]
    # Calcul des moyennes
    df["Montant_Compute"] = (df["Montant_Vide31"]/1.31 + df["Montant_HorsVide"])/2
    df["Avalant_Compute"] = (df["Avalant_Vide31"]/1.31 + df["Avalant_HorsVide"])/2
    df["Mixte_Compute"] = (df["Mixte_Vide31"]/1.31 + df["Mixte_HorsVide"])/2
    # Sélection des colonnes finales
    return df[["Puissance min HorsVide", "Puissance max HorsVide", "Montant_Compute", "Avalant_Compute", "Mixte_Compute"]].rename(columns={
        "Puissance min HorsVide": "Puissance min",
        "Puissance max HorsVide": "Puissance max"
    })

#### Tableau standardisée 
##### Consommation Automoteur L/t.km standardisée
Conso_Atm_Seine_Standard = conso_atm_standard(Conso_Atm_Seine_Vide_31,
                                              Conso_Atm_Seine_Hors_Vide)
Conso_Atm_Seine_Standard

Conso_Atm_PetiteSeine_Oise_Standard = conso_atm_standard(Conso_Atm_PetiteSeine_Oise_Vide_31,
                                                         Conso_Atm_PetiteSeine_Oise_Hors_Vide)
Conso_Atm_PetiteSeine_Oise_Standard

Conso_Atm_Rhone_Saone_Standard = conso_atm_standard(Conso_Atm_Rhone_Saone_Vide_31,
                                                    Conso_Atm_Rhone_Saone_Hors_Vide)
Conso_Atm_Rhone_Saone_Standard

Conso_Atm_Rhin_Standard = conso_atm_standard(Conso_Atm_Rhin_Vide_31,
                                             Conso_Atm_Rhin_Hors_Vide)
Conso_Atm_Rhin_Standard

Conso_Atm_Moselle_Standard = conso_atm_standard(Conso_Atm_Moselle_Vide_31,
                                                Conso_Atm_Moselle_Hors_Vide)
Conso_Atm_Moselle_Standard

Conso_Atm_Canal_Standard = conso_atm_standard(Conso_Atm_Canal_Vide_31,
                                              Conso_Atm_Canal_Hors_Vide)
Conso_Atm_Canal_Standard.columns = ["Capacité min", "Capacité max", 
                                    "GG_Compute", "MG_Compute", "PG_Compute"]
Conso_Atm_Canal_Standard

##### Consommation Pousseur L/t.km standardisée
Conso_Psr_Seine_Standard = conso_psr_standard(Conso_Psr_Seine_Vide_31,
                                              Conso_Psr_Seine_Hors_Vide)
Conso_Psr_Seine_Standard

Conso_Psr_PetiteSeine_Oise_Standard = conso_psr_standard(Conso_Psr_PetiteSeine_Oise_Vide_31,
                                                         Conso_Psr_PetiteSeine_Oise_Hors_Vide)
Conso_Psr_PetiteSeine_Oise_Standard

Conso_Psr_Rhone_Saone_Standard = conso_psr_standard(Conso_Psr_Rhone_Saone_Vide_31,
                                                    Conso_Psr_Rhone_Saone_Hors_Vide)
Conso_Psr_Rhone_Saone_Standard

Conso_Psr_Rhin_Standard = conso_psr_standard(Conso_Psr_Rhin_Vide_31,
                                             Conso_Psr_Rhin_Hors_Vide)
Conso_Psr_Rhin_Standard

Conso_Psr_Moselle_Standard = conso_psr_standard(Conso_Psr_Moselle_Vide_31,
                                                Conso_Psr_Moselle_Hors_Vide)
Conso_Psr_Moselle_Standard

Conso_Psr_Canal_Standard = conso_psr_standard(Conso_Psr_Canal_Vide_31,
                                              Conso_Psr_Canal_Vide_31)
Conso_Psr_Canal_Standard.columns = ["Puissance min", "Puissance max", 
                                    "GG_Compute", "MG_Compute", "PG_Compute"]
Conso_Psr_Canal_Standard