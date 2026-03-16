# Chargement des librairies
import pandas as pd

# Fonction pour créer les tableaux de consommation hors canal
## Entrée : liste de lignes (chaque ligne = [Capacité min, Capacité max, Montant, Avalant, Mixte])
def tableau_embarcation(type_embarcation, *lignes):
    type_embarcation = type_embarcation.lower()  # Normalisation
    if type_embarcation == "automoteur":
        colonnes = ["Capacité min", "Capacité max", "Montant", "Avalant", "Mixte"]
    elif type_embarcation == "pousseur":
        colonnes = ["Puissance min", "Puissance max", "Montant", "Avalant", "Mixte"]
    else:
        raise ValueError("Type_embarcation doit être 'Automoteur' ou 'Pousseur'")
    
    return pd.DataFrame(lignes, columns=colonnes)


# Fonction pour créer un tableau canal
def tableau_embarcation_canal(type_embarcation, nom_colonne, *lignes):
    type_embarcation = type_embarcation.lower()
    if type_embarcation == "automoteur":
        colonnes = ["Capacité min", "Capacité max", nom_colonne]
    elif type_embarcation == "pousseur":
        colonnes = ["Puissance min", "Puissance max", nom_colonne]
    else:
        raise ValueError("Type embarcation doit être 'Automoteur' ou 'Pousseur'")
    
    return pd.DataFrame(lignes,columns=colonnes)