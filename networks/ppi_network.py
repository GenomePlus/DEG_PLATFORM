import networkx as nx


def build_ppi_network(edges_df):

    G = nx.Graph()

    for _, row in edges_df.iterrows():

        gene1 = row["protein1"]
        gene2 = row["protein2"]
        score = float(row["score"])

        G.add_edge(gene1, gene2, weight=score)

    return G
