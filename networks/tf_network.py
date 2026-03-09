import networkx as nx


def build_tf_network(edges_df):

    G = nx.DiGraph()

    for _, row in edges_df.iterrows():

        tf = row["TF"]
        gene = row["target_gene"]

        G.add_edge(tf, gene)

    return G
