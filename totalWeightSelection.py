!pip install PyMaxFlow

import maxflow
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(n, weights, edges):
    G = nx.DiGraph()
    S = 'S'
    T = 'T'

    INF = '∞'   # for visualization only; not used in actual computation

    # Add nodes
    for i in range(n):
        G.add_node(i, label=f"P{i+1}\n{weights[i]}")

    G.add_node(S)
    G.add_node(T)

    # Source/sink edges
    for i in range(n):
        if weights[i] > 0:
            G.add_edge(S, i, capacity=weights[i])
        elif weights[i] < 0:
            G.add_edge(i, T, capacity=-weights[i])

    # Precedence constraints
    for u, v in edges:
        G.add_edge(u, v, capacity=INF)

    # Draw
    pos = nx.spring_layout(G, seed=42)  # for reproducible layout
    edge_labels = {(u, v): str(G[u][v]['capacity']) for u, v in G.edges()}
    node_labels = {node: G.nodes[node].get("label", str(node)) for node in G.nodes()}

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color='lightblue', node_size=2000, font_size=10, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Flow Network for Project Selection")
    plt.axis('off')
    plt.show()


def main():
    input_str = """6 7
    -3 -2 -7 -1 6 10
    1 2
    1 3
    1 4
    2 6
    3 5
    4 5
    4 6
    """
    data = input_str.split()

    idx = 0
    n, m = int(data[idx]), int(data[idx + 1])
    idx += 2

    weights = list(map(int, data[idx:idx + n]))
    idx += n

    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        edges.append((u, v))
        idx += 2

    # Initialize graph with n nodes
    g = maxflow.Graph[float](n, len(edges) + 2 * n)
    nodes = list(range(n))
    g.add_nodes(n)


    total_positive_weight = 0

    for i in range(n):
        if weights[i] > 0:
            g.add_tedge(nodes[i], 0, weights[i])  # source to node[i]
            total_positive_weight += weights[i]
        elif weights[i] < 0:
            g.add_tedge(nodes[i], -weights[i], 0)  # node[i] to sink

    INF = 1e10  # A very large number to simulate infinite capacity
    for u, v in edges:
        g.add_edge(nodes[u], nodes[v], INF, 0)

    flow = g.maxflow()

    print("Maximum total weight:", int(total_positive_weight - flow))
    draw_graph(n, weights, edges)


if __name__ == "__main__":
    main()
