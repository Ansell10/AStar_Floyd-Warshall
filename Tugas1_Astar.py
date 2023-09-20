import queue as Q
import sys,os
import networkx as nx
import matplotlib.pyplot as plt

grafik={
    'V1': [('V2', 2),('V4',1),('V3',8)],
    'V2': [('V3', 6),('V5', 1),('V1', 2)],
    'V3': [('V1',8),('V2', 6),('V4', 7), ('V5', 5),('V6',1),('V7',2)],
    'V4': [('V1',1),('V3', 7),('V7', 9)],
    'V5': [('V3', 5),('V6', 3),('V2', 1), ('V8', 2),('V9',9)],
    'V6': [('V3',1),('V5', 3),('V7', 4), ('V9', 6)],
    'V7': [('V6', 4),('V3', 2),('V4', 9),('V9', 3), ('V10', 1)],
    'V8': [('V5', 2),('V9', 7), ('V11', 9)],
    'V9': [('V6', 6),('V5',9),('V7', 3),('V8', 7),('V10', 1), ('V11', 2)],
    'V10': [('V9',1), ('V7', 1),('V11', 4)],
    'V11': [('V10',4),('V9',2),('V8',9)]
}

G = nx.Graph()

# Tambahkan node ke grafik
for node in grafik:
    G.add_node(node)

# Tambahkan edge ke grafik
for node, edges in grafik.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

heuristik = {
    'V1': 0,
    'V2': 0,
    'V3': 0,
    'V4': 0,
    'V5': 0,
    'V6': 0,
    'V7': 0,
    'V8': 0,
    'V9': 0,
    'V10': 0,
    'V11': 0
}

def astar(graph, init, goal):
    dikunjungi = []
    path = []
    prev = {}
    queue = Q.PriorityQueue()
    queue.put((0, init, None))
    totalcost = 0
    while queue:
        cost, node, prev_n = queue.get()
        if node not in dikunjungi:
            dikunjungi.append(node)
            prev[node] = prev_n
            if node == goal:              
                while prev[node] != None:  
                    path += [node]
                    for i, c in graph[node]:
                        if i == prev[node]:
                            totalcost += c
                    node = prev[node]
                path += [init]
                return totalcost, dikunjungi, prev, path[::-1]
            for i, c in graph[node]:
                if i not in dikunjungi:
                    total_cost = cost + c
                    h1 = heuristik[i]
                    total = total_cost + h1 - heuristik[node]
                    queue.put((total, i, node))


#awal = input("Vertex Awal: ")
#tujuan = input("Vertex Tujuan: ")
awal = "V1"
tujuan = "V11"

cost, dikunjungi, prev, path = astar(grafik, awal, tujuan)

# Inisialisasi grafik
G = nx.Graph()

# Tambahkan node ke grafik
for node in grafik:
    G.add_node(node)

# Tambahkan edge ke grafik
for node, edges in grafik.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)  # Sertakan bobot edge

# Tentukan posisi node secara manual sesuai dengan urutan vertikal
node_positions = {
    'V2': (2, 2),
    'V5': (3, 2),
    'V8': (4, 2),
    'V1': (1, 1),
    'V3': (2, 1),
    'V6': (3, 1),
    'V9': (4, 1),
    'V11': (5, 1),
    'V4': (2, 0),
    'V7': (3, 0),
    'V10': (4, 0)
}

# Inisialisasi warna node dan edge
node_colors = ['g' if node in dikunjungi else 'b' for node in G.nodes()]

# Mendapatkan semua edge yang termasuk dalam path terpendek
shortest_path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

# Menggambar edge, memberi warna merah hanya pada edge yang merupakan bagian dari path terpendek
edge_colors = ['r' if G.has_edge(node, neighbor) and ((node, neighbor) in shortest_path_edges or (neighbor, node) in shortest_path_edges) else 'k' for node, neighbor in G.edges()]

# Gambar node dan edge
nx.draw(G, node_positions, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=500)

# Tambahkan label bobot edge
edge_labels = {(node, neighbor): weight for node, neighbor, weight in G.edges(data='weight')}
nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_labels, label_pos=0.5)  # Atur label_pos ke 0.5

# Tampilkan grafik
plt.show()


cost, dikunjungi, prev, path = astar(grafik, awal, tujuan)
print("Solusi dengan A* Search\nNode yang dikunjungi:")
print(dikunjungi)
print("Path yang diikuti: " + "->".join(path))
print("Path cost dengan A* Search:", cost)
print("List dari node sebelum-sebelumnya:")
print(prev)