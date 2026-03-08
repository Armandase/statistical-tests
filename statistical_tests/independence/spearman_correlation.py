import numpy as np
import scipy.stats as stats

# Le coefficient de correlation de Spearman sert a mesurer le sens et la force de la relation monotone(basée sur leur rang) entre deux variables.

# On utilise le test de corrélation de spearman pour verifier s'il y a un liens entre les rangs des variables

# Condition:

# H0: il n'y a pas de corrélation entre les 2 variables
# avec r = 0

# Options pour H1: il y a une corrélation entre les 2 variables
# - Bilatérale : r≠0 (test le plus courant)

def main(X, Y, alpha):
    n = X.size
    if n != Y.size:
        print("Les deux variables doivent possédées autant de valeur.")
        return

    # récupère les index triés des données (ex-aequo = le rang moyen)
    rank_X = stats.rankdata(X)
    rank_Y = stats.rankdata(Y)

    # $r = 1 - \frac{6\sum_{i=1}^n d_i^2}{n(n^2 - 1)}$ avec $d_i = \text{rang}(x_i) - \text{rang}(y_i)$
    denominator = n * (n**2 - 1)
    if denominator == 0:
        print("Le coefficient de corrélation est indéfini (division par zéro).")
        return
    r = 1 - ( (6 * np.sum((rank_X - rank_Y)**2)) / denominator)
    print(f"Coefficient de corrélation de Spearman r = {r:.4f}")

    # il faut ensuite déterminer la statistique de test (la stat suit une loi de Student à n-2 degrès de liberté)
    # $ t=r\sqrt{\frac{n-2}{1-r^2}} $

    if abs(r) == 1:
        print(f"Corrélation parfaite (r={r}): le t de student tend vers l'infini, on rejette H0.")
        return

    t = r * np.sqrt((n - 2) / (1 - r**2))

    df = n - 2

    t_expected = stats.t.ppf(1 - alpha/2, df=df)
    p_value = 2 * stats.t.sf(np.abs(t), df=df)

    print(f"t: {t:.4f}\tt_critique: {t_expected:.4f} (alpha={alpha}, bilatéral)")

    if abs(t) > t_expected:
        print("REJETTE H0 (|t| > t_critique). Il existe une corrélation monotone significative entre les deux variables.")
    else:
        print("NE rejette PAS H0. On ne peut pas affirmer qu'il existe une corrélation monotone significative entre les deux variables.")

    print(f"p-valeur = {p_value:.4f}")
    if p_value < alpha:
        print(f"La p-valeur ({p_value:.4f}) est inférieure à alpha ({alpha}) : on rejette H0.")
    else:
        print(f"La p-valeur ({p_value:.4f}) est supérieure ou égale à alpha ({alpha}) : on ne rejette pas H0.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--alpha", '-a', type=float, default=0.05, help="significance level")
    args = parser.parse_args()

    x = np.array([12,15,17,18,20,21,22,26])
    y = np.array([14,25,20,35,45,30,60,95])
    main(x, y, args.alpha)