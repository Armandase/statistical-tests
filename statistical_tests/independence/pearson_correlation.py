import numpy as np
import scipy.stats as stats

# Le coefficient de Pearson sert a mesurer le sens et la force de la relation linéaire entre deux variables.

# On utilise le test de corrélation linéaire pour verifier s'il y a un liens entre les varaibles

# Condition:
# Liens linéaire entre les 2 variables
# Les 2 variables doivent suivre une distribution normal
# Pas d'outliers (données extrêmes)

# H0: il n'y a pas de relation linéaire entre les 2 variables
# avec r = 0

# Options pour H1: il y a une relation linéaire entre les 2 variables
# - Bilatérale : r≠0 (test le plus courant)
# - Unilatérale à droite : r>0 (corrélation positive)
# - Unilatérale à gauche : r<0 (corrélation négative)

def main(X, Y, alpha, h1):
    n = X.size
    if n != Y.size:
        print("Les deux variables doivent possédées autant de valeur.")
        return
    
    # $r = \frac{E(XY) - E(X)E(Y)}{\sqrt{E(X^2) - E(X)^2}\sqrt{E(Y^2) - E(Y)^2}} = \frac{Cov_{x,y}}{\sigma_x*\sigma_y}$
    
    denominator = np.sqrt(np.mean(X**2) - np.mean(X)**2) * np.sqrt(np.mean(Y**2) - np.mean(Y)**2)
    if denominator == 0:
        print("Le coefficient de corrélation est indéfini (division par zéro).")
        return
    r = (np.mean(X * Y) - np.mean(X) * np.mean(Y)) / denominator
    print(f"Coefficient de corrélation de Pearson r = {r:.4f}")

    # il faut ensuite déterminer la statistique de test (la stat suit une loi de Student à n-2 degrès de liberté)

    # $ t=r\sqrt{\frac{n-2}{1-r^2}} $ 
    
    t = r * np.sqrt((n - 2) / (1-r**2))
    print("t: ", t)

    df = n - 2

    t_expected = None
    p_value = None
    if h1 == "bilateral":
        t_expected = stats.t.ppf(1 - alpha/2, df=df)
        p_value = 2 * stats.t.sf(np.abs(t), df=df)
    elif h1 == "right":
        t_expected = stats.t.ppf(1 - alpha, df=df)
        p_value = stats.t.sf(t, df=df)
    elif h1 == "left":
        t_expected = stats.t.ppf(alpha, df=df)
        p_value = stats.t.cdf(t, df=df)
    else:
        print("Hypothèse alternative non reconnue. Utilisez 'bilateral', 'right' ou 'left'.")
        return

    print(f"t_critique: {t_expected:.4f} (alpha={alpha}, h1={h1})")

    if t < t_expected and h1 == "left":
        print("REJETTE H0 (t < t_critique). Il existe une corrélation négative significative entre les deux variables.")
    elif t > t_expected and h1 == "right":
        print("REJETTE H0 (t > t_critique). Il existe une corrélation positive significative entre les deux variables.")
    elif h1 == "bilateral" and (t < -t_expected or t > t_expected):
        print("REJETTE H0 (|t| > t_critique). Il existe une corrélation significative entre les deux variables.")
    else:
        print("NE rejette PAS H0. On ne peut pas affirmer qu'il existe une corrélation significative entre les deux variables.")

    print(f"p-valeur = {p_value:.4f}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--alpha", '-a', type=float, default=0.05, help="significance level")
    parser.add_argument("--h1", '-H', type=str, default="bilateral", help="alternative hypothesis: bilateral, right, left")
    args = parser.parse_args()

    # x = np.array([10, 7, 8])
    # y = np.array([13, 11, 9])
    x = np.array([1, 2, 3, 4, 8, 6,7, 8, 9])
    y = np.array([11, 12, 13, 14, 15, 16, 17, 18, 22])
    main(x, y, args.alpha, args.h1)