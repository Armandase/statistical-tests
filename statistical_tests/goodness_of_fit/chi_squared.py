import numpy as np
import scipy.special as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

# Test permettant de déterminer 
# a quelle point une distribution expérimentale ou observé correspond au attente

# Cas d'usage: count ou fréquence pour une variable catégorielle avec au moins 2 catégories

# Expected distribution
# White Black   Silver  Other
# 0.28  0.25    0.16    0.31

# Observed frequency (in nb sample):
# White Black   Silver  Other
# 39    29      24      48

# H0 hypothèse nulle est que la distribution correspond a "Expected distribution"
# H1 au moins une proba n'est pas égale à celle de la distribution attendue 
# α (0.05) seuil de signification (proba que le test rejette H0 alors que H0 est vraie)

# Conditions:
# $n ≥ 30$
# $$E_{i} ≥ 5 \forall i$$

# $E_{i} = nb\ sample \times p_i$

def main(O: np.ndarray, E=None, α=0.05):
    nb_categories = O.size
    nb_samples = O.sum()
    if E is None:
        # E = np.zeros(())
        # for i in range(nb_categories):
            # E[i] = (np.sum(O[i]) * np.sum(O[])) / np.sum(O)
        # print("E", E)
        exit()
    
    for i in range(nb_categories):
        E[i] = nb_samples * E[i]

    print(E.sum())
    if np.min(E) < 5:
        print("can't compute goodness of fit test with a cell frequency below 5")

    # somme des carrés des écarts relativisés (chi squared)

    # $χ^2 = \sum_{i=1}^{k} \frac{(O_{i} - E_{i})^2}{E_{i}}$
    
    χ = np.sum(((O - E) ** 2) / E)
    print("χ",  χ)
    # freq observé != freq théorique (χ = 0)

    # degres de liberté (corrélé  à la tolérence, décale la bosse de la courbe a droite)
    # $ df = (k  - 1)$ avec $k$ etant le nombre de catégories
    df = nb_categories - 1

    # Valeur critique : χ²_critique tel que P(χ² > χ²_critique) = α
    χ_crit = stats.chi2.ppf(1 - α, df=df)
    # PPF = En dessous de quelle valeur se trouvent p% des observations ?

    # p-valeur : probabilité d'obtenir un χ² aussi grand sous H0
    p_value = stats.chi2.sf(χ, df=df)   # sf = 1 - cdf

    print("\n--- Interprétation ---")
    print(f"χ²          = {χ:.4f}")
    print(f"χ²_critique = {χ_crit:.4f}  (α={α}, ν={df})")
    print(f"p-valeur    = {p_value:.4f}")

    if χ > χ_crit:   # équivalent à p_value < α
        print(f"REJETTE H0 (χ² > χ²_critique, p={p_value:.4f} < α={α}).")
        print("La distribution observée diffère significativement de la distribution attendue.")
    else:
        print(f"NE rejette PAS H0 (χ² ≤ χ²_critique, p={p_value:.4f} ≥ α={α}).")
        print("La distribution observée ne diffère pas significativement de la distribution attendue.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    args = parser.parse_args()

    observed = None
    observed = np.array([39, 29, 24, 48])
    # excepted = np.array([0.28, 0.25, 0.16, 0.31])
    excepted = np.array([0.25, 0.25, 0.25, 0.25])
    main(observed, E=excepted)