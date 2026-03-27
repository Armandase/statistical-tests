# Independence Tests

Independence tests are used to determine whether a relationship exists between two variables.

The choice of technique depends on the nature of the variables (nominal, qualitative, ordinal, or quantitative).

## Implemented Tests

### Chi-Squared Test (χ²)

The independence chi-squared test is used with two qualitative variables organized in a contingency table.

It determines if there is a significant relationship between two variables (where at least one is nominal or ordinal) in a population.
The test is based on sample data from a contingency table.

- **H₀ (Null Hypothesis):** No relationship between variables (they are independent).
- **H₁ (Alternative Hypothesis):** There is a significant relationship between variables.
- **α (Significance Level, typically 0.05):** Represents the probability of rejecting the null hypothesis when it is actually true.

#### Conditions:

$n ≥ 30$

$E_{ij} ≥ 5 \forall i,j$


$E_{ij} = \frac{Total_{Colonne} \times Total_{Ligne}}{Total}$


### Pearson correlation

- [x]  Test de corrélation de Pearson – mesure la dépendance linéaire entre deux variables quantitatives (avec hypothèse de normalité).


### Spearman correlation
- [x]  Test de corrélation de Spearman – basé sur les rangs, évalue une dépendance monotone.

### Exact of Fisher
- [ ]  Test exact de Fisher – adapté aux petits échantillons (tableaux 2×2).
