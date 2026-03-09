"""
Network utilities for PPI analysis
"""

import networkx as nx


def build_graph_from_edges(edge_df,
                           source_col="source",
                           target_col="target",
                           weight_col=None):
    """
    Convert edge table to NetworkX graph
    """

    G = nx.Graph()

    for _, row in edge_df.iterrows():

        source = row[source_col]
        target = row[target_col]

        if weight_col:
            weight = row[weight_col]
            G.add_edge(source, target, weight=weight)
        else:
            G.add_edge(source, target)

    return G


def get_first_neighbors(G, gene):
    """
    Return first neighbor genes
    """
    if gene not in G:
        return []

    return list(G.neighbors(gene))


def network_density(G):
    """
    Calculate network density
    """
    return nx.density(G)


def largest_connected_component(G):
    """
    Return largest connected component
    """

    if len(G.nodes) == 0:
        return G

    largest_cc = max(nx.connected_components(G), key=len)

    return G.subgraph(largest_cc).copy()
