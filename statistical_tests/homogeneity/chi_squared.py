import numpy as np
import scipy.special as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

# Test statistiques d'homogénéité entre deux groupes différents et calculer si les distributions de ces groupes, pour une variable qualitative, sont homogènes(similaires) ou pas.
# Déterminer si la distribution d'une variable catégorielle est la même (similaire) à travers différentes populations ou groupes.
# Les étapes sont similaire au test d'indépendance, mais dans le test d'homogénéité, on teste si la distribution d'une variable catégorielle est la même à travers différentes populations ou groupes.

# H0 pas de différence entre les distributions des groupes
# H1 il existe une différence entre les distributions des groupes
# α (0.05) seuil de signification (proba que le test revele qu'il existe une différence entre les groupes alors qu'il n'en existe pas réelement)

# Conditions:
# pas nécessairement même taille d'échantillon
# $n ≥ 30$
# $$E_{ij} ≥ 5 \forall i,j$$


def main(O, α=0.05):
    # E représente les données dans le cas où H0 est vrai (pas de différence entre les groupes)
    
    # $E_{ij} = \frac{Total_{Colonne} \times Total_{Ligne}}{Total}$

    E = np.zeros_like(O)
    rows, cols = O.shape
    for i in range(rows): 
        for j in range(cols):
            E[i][j] = (np.sum(O[:, j]) * np.sum(O[i, :])) / np.sum(O)
    print("E", E)

    # somme des carrés des écarts relativisés (chi squared)

    # $χ^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$

    χ = np.sum(((O - E) ** 2) / E)    
    print("χ",  χ)
    # freq observé != freq théorique (χ = 0)

    # plus X² est grand, plus les données sont éloignées de ce que l'on attendrait si H0 était vrai (pas de différence entre les groupes)

    # degres de liberté (corrélé  à la tolérence, décale la bosse de la courbe a droite)
    # ν = (nb ligne - 1) * (nb col - 1) 
    v = (rows - 1) * (cols - 1)

    # v et alpha servent a déterminer la valeur critique
    print("ν", v)

    # Interprétation: Avec un seuil de signification de 5%,
    # on ne peut pas affimer qu'il exstait une différence entre les groupes ... et ...

    # Valeur critique : χ²_critique tel que P(χ² > χ²_critique) = α
    χ_crit = stats.chi2.ppf(1 - α, df=v)
    # PPF = En dessous de quelle valeur se trouvent p% des observations ?

    # p-valeur : probabilité d'obtenir un χ² aussi grand sous H0
    p_value = stats.chi2.sf(χ, df=v)   # sf = 1 - cdf

    print("\n--- Interprétation ---")
    print(f"χ²          = {χ:.4f}")
    print(f"χ²_critique = {χ_crit:.4f}  (α={α}, ν={v})")
    print(f"p-valeur    = {p_value:.4f}")

    if χ > χ_crit:   # équivalent à p_value < α
        print(f"REJETTE H0 (χ² > χ²_critique, p={p_value:.4f} < α={α}).")
        print("Il existe une différence significative entre les groupes.")
    else:
        print(f"NE rejette PAS H0 (χ² ≤ χ²_critique, p={p_value:.4f} ≥ α={α}).")
        print("On ne peut pas affirmer qu'il existe une différence entre les groupes.")


#           Gauché  Droitier    Total
# sport     30      10          40
# science   15      25          40
# droit     15      5           20
# total     60      40          100
def get_data():
    return np.array([[30, 10],
                     [15, 25],
                     [15, 5]])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level (default: 0.05)")
    args = parser.parse_args()

    observed = get_data()
    main(observed, α=args.alpha)