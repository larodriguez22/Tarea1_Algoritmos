import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskalMST(adj_matrix):
    V = len(adj_matrix)
    edges = []

    for i in range(V):
        for j in range(i + 1, V):
            if adj_matrix[i][j] != 0:
                edges.append([i, j, adj_matrix[i][j]])

    edges.sort(key=lambda item: item[2])
    
    parent = list(range(V))
    rank = [0] * V
    result = []
    e = 0
    i = 0

    while e < V - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    
    minimumCost = 0
    print("Arcos dobles construidos en el MST:")
    for u, v, weight in result:
        minimumCost += weight
        print(f"{u} -- {v} == {weight}")
    print("Costo del Minimum Spanning Tree:", minimumCost)
    return result

def read_adjacency_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)
    return matrix

def generate_random_adjacency_matrix(size, max_weight=20):
    matrix = np.random.randint(0, max_weight, size=(size, size))
    np.fill_diagonal(matrix, 0)  # Diagonal principal a cero (no hay auto-bucles)
    upper_triangle = np.triu_indices(size, k=1)
    matrix[upper_triangle] = matrix.T[upper_triangle]  # La matriz es simétrica
    return matrix

def save_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def visualize_graph(adjacency_matrix, mst_edges):
    G = nx.Graph()

    for i in range(len(adjacency_matrix)):
        G.add_node(i)

    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            weight = adjacency_matrix[i][j]
            if weight > 0:
                G.add_edge(i, j, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

    mst_edges_set = set((u, v) for u, v, _ in mst_edges)
    edge_colors = ['red' if (u, v) in mst_edges_set or (v, u) in mst_edges_set else 'black' for u, v, _ in G.edges(data=True)]
    edge_widths = [3 if (u, v) in mst_edges_set or (v, u) in mst_edges_set else 1 for u, v, _ in G.edges(data=True)]

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', edge_color=edge_colors, width=edge_widths)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Visualización del Grafo")
    plt.show()

if __name__ == '__main__':
    num = int(input("Subio un archivo con la matriz (1) o desea generar un grafo (1): "))
    if num == 1:
      file_path = sys.argv[1]
    elif num == 2:
      matrix_size = int(input("Defina el maximo de nodos que quiera de la matriz: ")) # 5
      max_weight = 100
      file_path = 'random_matrix.txt'
      random_matrix = generate_random_adjacency_matrix(matrix_size, max_weight)
      save_matrix_to_file(random_matrix, file_path)  
      print("Matriz aleatoria generada")
    try:
        adjacency_matrix = read_adjacency_matrix(file_path)
        mst_edges = kruskalMST(adjacency_matrix)
        visualize_graph(adjacency_matrix, mst_edges)
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)