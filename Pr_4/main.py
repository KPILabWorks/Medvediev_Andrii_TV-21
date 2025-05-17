import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import math

# 1. Create the graph model of a power grid
def create_power_grid_graph():
    G = nx.powerlaw_cluster_graph(n=50, m=3, p=0.1)
    return G

# 2. Simulate node failures
def simulate_failures(G, mode='random', steps=10):
    original_size = len(max(nx.connected_components(G), key=len))
    sizes = [original_size]
    G_copy = G.copy()

    for i in range(steps):
        if len(G_copy) == 0:
            sizes.append(0)
            continue

        # Select a node to remove
        if mode == 'random':
            node = random.choice(list(G_copy.nodes()))
        elif mode == 'targeted':
            node = max(G_copy.degree, key=lambda x: x[1])[0]
        else:
            raise ValueError("Mode must be 'random' or 'targeted'")

        G_copy.remove_node(node)

        # Compute the size of the largest connected component
        if len(G_copy) > 0:
            largest_cc_size = len(max(nx.connected_components(G_copy), key=len))
        else:
            largest_cc_size = 0

        sizes.append(largest_cc_size)

    return sizes

# 3. Statistical reliability estimate
def statistical_reliability(lambd=0.05, t=10):
    return math.exp(-lambd * t)

# 4. Main function
def main():
    print(" Creating the power grid graph model...")
    G = create_power_grid_graph()
    total_nodes = G.number_of_nodes()
    total_edges = G.number_of_edges()

    print(f" Number of nodes (substations): {total_nodes}")
    print(f" Number of edges (connections): {total_edges}")

    # Visualize the graph
    plt.figure(figsize=(8, 6))
    nx.draw_spring(G, node_size=50, with_labels=False)
    plt.title("Power Grid Model (Graph Structure)")
    plt.legend(["Nodes = substations, edges = connections"], loc='lower right')
    plt.show()

    # Simulate failures
    print("\n Simulating random and targeted failures...")
    steps = 15
    random_failures = simulate_failures(G, mode='random', steps=steps)
    targeted_failures = simulate_failures(G, mode='targeted', steps=steps)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(random_failures, label='Random Failures', marker='o', linewidth=2)
    plt.plot(targeted_failures, label='Targeted Failures (high-degree nodes)', marker='x', linewidth=2)
    plt.xlabel("Number of removed nodes")
    plt.ylabel("Size of the largest connected component")
    plt.title("Network Robustness Against Failures")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Statistical analysis
    lambd = 0.05
    t = 10
    reliability = statistical_reliability(lambd, t)
    print(f"\n Statistical reliability estimate at λ = {lambd}, t = {t}:")
    print(f"   R(t) = exp(-λt) = {reliability:.4f}")

    # Result analysis
    print("\n Analysis:")
    print(f"• Initial largest component size: {random_failures[0]}")
    print(f"• After {steps} random failures: {random_failures[-1]}")
    print(f"• After {steps} targeted failures: {targeted_failures[-1]}")

    if targeted_failures[-1] < random_failures[-1]:
        print(" Conclusion: The network is more vulnerable to targeted attacks on critical nodes.")
    else:
        print(" Conclusion: The network remains robust even under targeted attacks.")

    print("\n The statistical method provides a general idea of reliability,")
    print("   but the graph-based analysis identifies which nodes are critical.")

if __name__ == "__main__":
    main()