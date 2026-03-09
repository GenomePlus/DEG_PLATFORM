import networkx as nx
import pandas as pd


def calculate_network_metrics(G):

    """
    Compute standard network metrics
    """

    metrics = {}

    metrics["degree"] = dict(G.degree())
    metrics["degree_centrality"] = nx.degree_centrality(G)
    metrics["betweenness_centrality"] = nx.betweenness_centrality(G)
    metrics["closeness_centrality"] = nx.closeness_centrality(G)
    metrics["eigenvector_centrality"] = nx.eigenvector_centrality(G, max_iter=1000)
    metrics["clustering_coefficient"] = nx.clustering(G)

    df = pd.DataFrame(metrics)

    df["gene"] = df.index

    return df.reset_index(drop=True)
