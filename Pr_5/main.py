import networkx as nx
import matplotlib.pyplot as plt

def create_relationship_graph():
    G = nx.Graph()
    objects = ["Server", "Router", "PC1", "PC2", "Printer", "Switch", "Firewall"]
    connections = [
        ("Server", "Switch"),
        ("Router", "Switch"),
        ("PC1", "Switch"),
        ("PC2", "Switch"),
        ("Printer", "Switch"),
        ("Switch", "Firewall"),
        ("Firewall", "Router")
    ]
    G.add_nodes_from(objects)
    G.add_edges_from(connections)
    return G

def analyze_graph(G):
    print(" Network Analysis")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Degree of each node: {dict(G.degree())}")
    print(f"Is the graph connected? {'Yes' if nx.is_connected(G) else 'No'}")
    print(f"Average shortest path length: {nx.average_shortest_path_length(G):.2f}")
    print(f"Network diameter: {nx.diameter(G)}")
    print(f"Clustering coefficient: {nx.average_clustering(G):.2f}")

def get_node_style():
    return {
        'Server':      ('red', 's'),
        'Router':      ('orange', '^'),
        'Firewall':    ('orange', '^'),
        'PC1':         ('blue', 'o'),
        'PC2':         ('blue', 'o'),
        'Printer':     ('purple', 'D'),
        'Switch':      ('green', 'h')
    }

def visualize_graph(G):
    pos = nx.spring_layout(G, seed=42, k=0.6)
    degrees = dict(G.degree())
    node_styles = get_node_style()

    plt.figure(figsize=(12, 9))

    # Draw nodes by type (colors and shapes)
    for node, (color, shape) in node_styles.items():
        nodes_of_type = [n for n in G.nodes() if n == node]
        nx.draw_networkx_nodes(
            G, pos, nodelist=nodes_of_type,
            node_color=color, node_shape=shape,
            node_size=[500 + degrees[n]*300 for n in nodes_of_type],
            label=f"{node}",
            alpha=0.9
        )

    # Draw edges
    nx.draw_networkx_edges(G, pos, width=2.0, edge_color="gray", alpha=0.7)

    # Labels for nodes
    for node, (x, y) in pos.items():
        label = f"{node}\n(d={degrees[node]})"
        plt.text(x, y - 0.07, label, fontsize=9, ha='center', va='center')

    # Legend formatting
    # Reduce the size of markers in the legend by half
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, labels, loc='upper left', fontsize=12, title="Device Types", title_fontsize=14, markerscale=0.5)

    plt.title(" Network Topology: Typed Object Interconnections", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    G = create_relationship_graph()
    analyze_graph(G)
    visualize_graph(G)

if __name__ == "__main__":
    main()

