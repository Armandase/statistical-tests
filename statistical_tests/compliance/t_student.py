import numpy as np
import scipy.special as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

# Test statistiques permettant de savoir si la moyenne d'un groupe a une différence 
# significative avec une valeur donnée

# H0 $\mu = \mu_0$ la moyen théorique est égale la moyenne calculé/données
# H1 3 options:
# - $\mu < \mu_0$ (moyenne + faible que valeur de ref)
# - $\mu > \mu_0$ (moyenne + élevé que valeur de ref)
# - $\mu = \mu_0$ (la moyenne théorique et donné sont différentes) 

# Conditions:
# observations indépendantes (tirages aléatoires)
# pas d'outliers 
# distibution normale des données
# si n > 30 on peut utiliser le test de Student même si les données ne sont pas normales (TCL)

def main(avg, avg_observed, std, n, α=0.05, h1='bilateral'):


    # $t = \frac{\mu - \mu_0}{\frac{\sigma}{\sqrt{n}}}$

    denominator = std / np.sqrt(n)
    if denominator == 0:
        print("La variance est nulle, le test de Student n'est pas applicable.")
        return
    t = (avg_observed - avg) / denominator

    # degres de liberté
    df = (n - 1)

    t_theorical = None
    p_value = None
    if h1 == "bilateral":
        t_theorical = stats.t.ppf(1 - α/2, df=df)
        p_value = 2 * stats.t.sf(np.abs(t), df=df)
    elif h1 == "right":
        t_theorical = stats.t.ppf(1 - α, df=df)
        p_value = stats.t.sf(t, df=df)
    elif h1 == "left":
        t_theorical = stats.t.ppf(α, df=df)
        p_value = stats.t.cdf(t, df=df)
    else:
        print("Hypothèse alternative non reconnue. Utilisez 'bilateral', 'right' ou 'left'.")
        return

    print("\n--- Interprétation ---")
    print(f"t          = {t:.4f}")
    print(f"t_critique = {t_theorical:.4f}  (α={α}, df={df})")
    print(f"p-valeur   = {p_value:.4f}")

    if h1 == "left" and t < t_theorical:
        print("REJETTE H0 (t < t_critique) : la moyenne observée est significativement inférieure à la valeur de référence.")
    elif h1 == "right" and t > t_theorical:
        print("REJETTE H0 (t > t_critique) : la moyenne observée est significativement supérieure à la valeur de référence.")
    elif h1 == "bilateral" and (t < -t_theorical or t > t_theorical):
        print("REJETTE H0 (|t| > t_critique) : la moyenne observée est significativement différente de la valeur de référence.")
    else:
        print("NE rejette PAS H0 : on ne peut pas affirmer que la moyenne diffère de la valeur de référence.")

    if p_value < α:
        print(f"\tLa p-valeur ({p_value:.4f}) est inférieure à alpha ({α}) : on rejette H0.")
    else:
        print(f"\tLa p-valeur ({p_value:.4f}) est supérieure ou égale à alpha ({α}) : on ne rejette pas H0.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--avg", '-a', type=float, default=19, help="theorcial average")
    parser.add_argument("--observed_avg", '-o', type=float, default=20.07, help="Observed average")
    parser.add_argument("--std", '-s', type=float, default=5.07, help="Std")
    parser.add_argument("--n", '-n', type=float, default=150, help="number of samples")
    parser.add_argument("--alpha", '-al', type=float, default=0.05, help="significance level")
    parser.add_argument("--h1", '-H', type=str, default="bilateral", help="alternative hypothesis: bilateral, right, left")
    args = parser.parse_args()

    main(args.avg, args.observed_avg, args.std, args.n, args.alpha, args.h1)