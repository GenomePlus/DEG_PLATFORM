import networkx as nx
import pandas as pd


def degree_centrality(G):
    return nx.degree_centrality(G)


def betweenness_centrality(G):
    return nx.betweenness_centrality(G)


def closeness_centrality(G):
    return nx.closeness_centrality(G)


def eigenvector_centrality(G):
    return nx.eigenvector_centrality(G, max_iter=1000)


def stress_centrality(G):

    stress = {}
    for node in G.nodes():
        stress[node] = 0

    for s in G.nodes():
        paths = nx.single_source_shortest_path(G, s)

        for p in paths.values():
            for node in p:
                stress[node] += 1

    return stress


def radiality(G):

    results = {}

    for node in G.nodes():

        path_lengths = nx.single_source_shortest_path_length(G, node)

        total = sum(path_lengths.values())

        results[node] = total

    return results


def eccentricity(G):
    return nx.eccentricity(G)


def clustering_coefficient(G):
    return nx.clustering(G)


def mcc(G):

    mcc_scores = {}

    for node in G.nodes():

        neighbors = list(G.neighbors(node))

        subgraph = G.subgraph(neighbors)

        mcc_scores[node] = subgraph.number_of_edges()

    return mcc_scores


def dmnc(G):

    dmnc_scores = {}

    for node in G.nodes():

        neighbors = list(G.neighbors(node))

        subgraph = G.subgraph(neighbors)

        n = subgraph.number_of_nodes()

        e = subgraph.number_of_edges()

        if n > 1:
            dmnc_scores[node] = e / (n ** 1.7)
        else:
            dmnc_scores[node] = 0

    return dmnc_scores


def mnc(G):

    scores = {}

    for node in G.nodes():

        neighbors = list(G.neighbors(node))

        subgraph = G.subgraph(neighbors)

        scores[node] = subgraph.number_of_edges()

    return scores


def epc(G):

    scores = {}

    for node in G.nodes():

        neighbors = list(G.neighbors(node))

        scores[node] = len(neighbors)

    return scores


def run_all_cytohubba(G):

    results = {
        "Degree": degree_centrality(G),
        "Betweenness": betweenness_centrality(G),
        "Closeness": closeness_centrality(G),
        "Eigenvector": eigenvector_centrality(G),
        "Stress": stress_centrality(G),
        "Radiality": radiality(G),
        "Eccentricity": eccentricity(G),
        "Clustering": clustering_coefficient(G),
        "MCC": mcc(G),
        "DMNC": dmnc(G),
        "MNC": mnc(G),
        "EPC": epc(G),
    }

    df = pd.DataFrame(results)

    df["gene"] = df.index

    return df.sort_values("Degree", ascending=False)
