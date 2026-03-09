import networkx as nx


def integrate_networks(ppi, mirna, tf):

    combined = nx.compose(ppi, mirna)
    combined = nx.compose(combined, tf)

    return combined
