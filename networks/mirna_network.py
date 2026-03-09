import networkx as nx


def build_mirna_network(edges_df):

    G = nx.DiGraph()

    for _, row in edges_df.iterrows():

        mirna = row["miRNA"]
        gene = row["target_gene"]

        G.add_edge(mirna, gene)

    return G
