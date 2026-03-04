import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# Chi-squared distribution

# $$X = \sum_{i=1}^{k} Z_i^2$$ 

# Normal distrib centred & reduced
# E(x) = 0
# Var(x) = 1

nb_samples = 10000

# discrete distribution
def discrete(degrees_of_freedom):
    sum_list = []
    cumulative = np.zeros(nb_samples)
    for i in range(degrees_of_freedom):
        sample = np.random.normal(loc=0, scale=1, size=nb_samples)
        cumulative = cumulative + sample**2
        sum_list.append(cumulative)

    # plot each histogram based on the degree of freedom
    fig = plt.figure(figsize=(degrees_of_freedom*5, 5))
    for i in range(degrees_of_freedom):
        ax = fig.add_subplot(1, degrees_of_freedom, i+1)
        ax.hist(sum_list[i], bins=30, density=True, alpha=0.6, color='g')
        ax.set_title(f"Degrees of Freedom: {i+1}")
    plt.tight_layout()
    plt.show()


# probability density function (PDF)

# $$ f(x) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{k/2 - 1} e^{-x/2}$$ 

def pdf(x, k):
    return 1 / (2**(k/2) * sp.gamma(k/2)) * x**(k/2-1) * np.exp(-x / 2)

def continuous(degrees_of_freedom):
    x = np.linspace(0.01, 30, 1000)
    fig, ax = plt.subplots(figsize=(10, 6))
    for k in range(1, degrees_of_freedom + 1):
        ax.plot(x, pdf(x, k), alpha=0.8, label=f"k={k}")
    ax.set_ylim(0, 0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("PDF")
    ax.set_title("Chi-squared PDF")
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chi-squared distribution example")
    parser.add_argument("--degrees-of-freedom", '-d', type=int, default=9, help="degree of freedom")
    args = parser.parse_args()
    continuous(args.degrees_of_freedom)