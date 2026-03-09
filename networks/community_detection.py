import networkx as nx
import pandas as pd
import community as community_louvain


def detect_communities(G):

    """
    Detect network communities using Louvain clustering
    """

    partition = community_louvain.best_partition(G)

    community_df = pd.DataFrame({
        "node": list(partition.keys()),
        "community": list(partition.values())
    })

    return community_df
