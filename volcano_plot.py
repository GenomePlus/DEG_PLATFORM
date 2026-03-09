import matplotlib.pyplot as plt
import numpy as np


def generate_volcano_plot(df):

    fig, ax = plt.subplots(figsize=(8,6), dpi=300)

    x = df["log2FoldChange"]
    y = -np.log10(df["pvalue"])

    ax.scatter(x, y, alpha=0.7)

    ax.set_xlabel("Log2 Fold Change")
    ax.set_ylabel("-Log10 P-value")

    ax.axhline(-np.log10(0.05), linestyle="--")

    return fig
