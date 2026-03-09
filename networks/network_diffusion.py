import networkx as nx
import numpy as np
import pandas as pd


def random_walk_with_restart(G, seed_genes, restart_prob=0.7, max_iter=50):

    """
    Network diffusion using Random Walk with Restart
    """

    nodes = list(G.nodes())

    n = len(nodes)

    adjacency = nx.to_numpy_array(G)

    degree = adjacency.sum(axis=1)

    transition = adjacency / degree[:, None]

    p0 = np.zeros(n)

    for gene in seed_genes:

        if gene in nodes:
            idx = nodes.index(gene)
            p0[idx] = 1

    p0 = p0 / p0.sum()

    p = p0.copy()

    for _ in range(max_iter):

        p = (1 - restart_prob) * np.dot(transition.T, p) + restart_prob * p0

    diffusion_scores = pd.DataFrame({
        "gene": nodes,
        "diffusion_score": p
    })

    diffusion_scores = diffusion_scores.sort_values(
        "diffusion_score",
        ascending=False
    )

    return diffusion_scores
