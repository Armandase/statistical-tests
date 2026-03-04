import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# Test statistiques pour variables qualitatives dans un tableau de contingence.

# def:
# Test permettant de déterminer s'il existe un lien entre 
# deux variables (dont au moins une est à nominale ou ordinale) dans une population,
# à partir des données d'un échantillon de cette population (tableau de contingence)

# probability density function (PDF)

# $$ f(x) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{k/2 - 1} e^{-x/2}$$ 

def pdf(x, k):
    return 1 / (2**(k/2) * sp.gamma(k/2)) * x**(k/2-1) * np.exp(-x / 2)

# Sexe      niveau scolaire     total
#       college lycee   univ
# femme 10      7       8       25  
# homme 13      11      9       33
# total 23      18      17      58
def get_exemple():
    data = {
    "sexe_niveau_scolaire": {
    "femme": { "college": 10, "lycee": 7, "univ": 8, "total": 25 },
    "homme": { "college": 13, "lycee": 11, "univ": 9, "total": 33 },
    "total": { "college": 23, "lycee": 18, "univ": 17, "total": 58 }
      }
    }



# H0 pas de lien entre les variables
# H1 un lien existe entre les variables étudié
# α (0.05) seuil de signification (proba que le test revele qu'il existe un lien entre les 2 var alors qu'il en n'existe pas réelement)

# Conditions:
# $n ≥ 30$
# $$T_{ij} ≥ 5 \forall i,j$$
def main(O, α=0.05, rows=2, cols=2):

    # $E_{ij} = \frac{Total_{Colonne} \times Total_{Ligne}}{Total}$
    
    E = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            E[i][j] = (np.sum(O[:, j]) * np.sum(O[i, :])) / np.sum(O)
    print("E", E)

    # somme des carrés des écarts relativisés (chi squared)

    # $χ^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$
    
    χ = np.sum(((O - E) ** 2) / E)
    print("χ",  χ)
    # freq observé != freq théorique (χ = 0)

    # Si pas de lien entre les variables, fortes chances que la val du χ^2 soit faible 
    # Si pas de lien entre les variables, faibles chances que la val du χ^2 soit élevé 
    # On détermine une valeur critique χ^2,
    # au dela de laquel on va considérer que la val du χ^2 est tellement élévé/improbable 
    # qu'on considère qu'il y a un lien entre les valeurs justifiant des écarts


    # degres de liberté (corrélé  à la tolérence, décale la bosse de la courbe a droite)
    # ν = (nb ligne - 1) * (nb col - 1) 
    v = (rows - 1) * (cols - 1)

    # v et alpha servent a déterminer la valeur critique
    print("ν", v)

    # if X^2 > valeur critique => rejette H0

    # si on ne rejette pas: 
    # Interprétation: Avec un seuil de signification de 5%,
    # on ne peut pas affimer qu'il exstait un lien entre ... et ... 


    # Coeff de contingence et coefficient de Cramér
    # Nombres servant à déterminer l'instensité d'un lien 
    # statistique existant entre deux variables dont au moins
    # une a une echelle nominale ou ordinale

    # $C = \sqrt{\frac{χ^2}{n+χ^2}}$

    C = np.sqrt(χ / (np.sum(O) + χ))
    print("C", C)

    # V = 

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--degrees-of-freedom", '-d', type=int, default=9, help="degree of freedom")
    parser.add_argument("--row", '-r', type=int, default=2, help="nb row")
    parser.add_argument("--col", '-c', type=int, default=2, help="nb col")
    args = parser.parse_args()

    observed = None
    observed = np.array([[10, 7, 8],
                         [13, 11, 9]])
    main(observed, args.degrees_of_freedom, args.row, args.col)