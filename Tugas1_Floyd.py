import math
import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

def floyd_warshall(n, edges):
    rn = range(n)
    dist = [[math.inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    
    for i in rn:
        dist[i][i] = 0
        
    for u, v, w in edges:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1

    # Menjalankan algoritma Floyd-Warshall
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]

    # Cari nodes yang termasuk dalam jalur terpendek dari v1 (0) ke v11 (10)
    start_node = 0  # v1
    end_node = 10   # v11
    shortest_path_nodes = [start_node]
    while shortest_path_nodes[-1] != end_node:
        shortest_path_nodes.append(nxt[shortest_path_nodes[-1]][end_node])

    # Membuat grafik
    G = nx.Graph()

    # Menambahkan node ke grafik
    for i in rn:
        G.add_node(i)  # Node dinamai 0, 1, ..., 10

    # Menambahkan edge ke grafik
    for u, v, w in edges:
        G.add_edge(u - 1, v - 1, weight=w)

    # Mengatur posisi node sesuai dengan urutan yang diminta
    node_positions = {
        0: (1, 1),   # v1
        1: (2, 2),   # v2
        2: (2, 1),   # v3
        3: (2, 0),   # v4
        4: (3, 2),   # v5
        5: (3, 1),   # v6
        6: (3, 0),   # v7
        7: (4, 2),   # v8
        8: (4, 1),   # v9
        9: (4, 0),   # v10
        10: (5, 1)   # v11
    }

    # Menggambar grafik dengan label
    labels = {i: f'v{i + 1}' for i in rn}  # Menggunakan indeks dimulai dari 1
    edge_labels = {(u - 1, v - 1): w for u, v, w in edges}  # Sesuaikan indeks
    edge_colors = ['r' if (u, v) in zip(shortest_path_nodes, shortest_path_nodes[1:]) else 'k' for u, v in G.edges()]

    # Menggambar nodes
    nx.draw_networkx_nodes(G, node_positions, node_color='blue', node_size=500)

    # Menggambar edges
    nx.draw_networkx_edges(G, node_positions, edge_color=edge_colors, width=2)

    # Menggambar labels
    nx.draw_networkx_labels(G, node_positions, labels, font_size=12, font_color='black')

    # Menggambar edge labels (berisi bobot)
    nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_labels, font_color='red')

    plt.title("Grafik Hasil Floyd-Warshall")
    plt.show()

    # Cetak nodes yang termasuk dalam jalur terpendek
    print("\nNodes dalam jalur terpendek dari v1 ke v11:", ' -> '.join(f'v{node + 1}' for node in shortest_path_nodes))
    
    # Cetak cost akhir dari jalur terpendek
    shortest_path_cost = dist[start_node][end_node]
    print("Cost akhir dari jalur terpendek dari v1 ke v11:", shortest_path_cost)

if __name__ == '__main__':
    # Daftar edges untuk grafik v1 hingga v11
    edges = [
        [1, 2, 2],
        [1, 4, 1],
        [1, 3, 8],
        [2, 3, 6],
        [2, 5, 1],
        [3, 4, 7],
        [3, 5, 5],
        [3, 6, 1],
        [3, 7, 2],
        [4, 7, 9],
        [5, 6, 3],
        [5, 8, 2],
        [5, 9, 9],
        [6, 7, 4],
        [6, 9, 6],
        [7, 9, 3],
        [7, 10, 1],
        [8, 9, 7],
        [8, 11, 9],
        [9, 10, 1],
        [9, 11, 2],
        [10, 11, 4]
    ]

    floyd_warshall(11, edges)
