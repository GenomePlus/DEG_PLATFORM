import matplotlib.pyplot as plt


def enrichment_barplot(df):

    fig, ax = plt.subplots(figsize=(8,6), dpi=300)

    top = df.head(10)

    ax.barh(top["pathway"], top["combined_score"])

    ax.set_xlabel("Combined Score")

    return fig


def enrichment_piechart(df):

    fig, ax = plt.subplots(figsize=(6,6), dpi=300)

    top = df.head(10)

    ax.pie(top["combined_score"], labels=top["pathway"])

    return fig
