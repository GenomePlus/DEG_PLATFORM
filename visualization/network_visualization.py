from pyvis.network import Network
import tempfile


def visualize_network(G):

    net = Network(height="600px", width="100%")

    for node in G.nodes():
        net.add_node(node)

    for edge in G.edges():
        net.add_edge(edge[0], edge[1])

    temp_file = tempfile.NamedTemporaryFile(delete=False)

    net.save_graph(temp_file.name)

    return temp_file.name
