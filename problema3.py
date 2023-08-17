import sys
import networkx as nx
import matplotlib.pyplot as plt

def leerArchivo(archivo):
    archivo = open(archivo, "r")
    lineas = archivo.readlines()
    lineas = [linea.strip() for linea in lineas]
    lineas = [linea.split(",") for linea in lineas]
    archivo.close()
    return lineas

def crearGrafo(lineas):
    grafo = {}
    for i in lineas:
        persona1 = i[0]
        persona2 = i[1]
        if persona1 not in grafo:
            grafo[persona1] = []
        if persona2 not in grafo:
            grafo[persona2] = []
        
        grafo[persona1].append(persona2)
        grafo[persona2].append(persona1)

    return grafo

def imprimirGrafo(grafo):
    for vertice in grafo:
        print(vertice, ":", grafo[vertice])

def hayFiesta(grafo, verticeInicial):
    colores = {nombre : -1 for nombre in grafo.keys()}
    cola = []
    cola.append(verticeInicial)
    colores[verticeInicial] = 1
    while len(cola) > 0 or list(colores.values()).count(-1) > 0:
        vertice = cola.pop(0)
        for adyacente in grafo[vertice]:
            if colores[adyacente] == -1:
                colores[adyacente] = 1 - colores[vertice]
                cola.append(adyacente)
            elif colores[adyacente] == colores[vertice]:
                return (False, [], [])
        
        if len(cola) == 0 and list(colores.values()).count(-1) > 0:
            for key in colores:
                if colores[key] == -1:
                    cola.append(key)
                    colores[key] = 1
                    break
    
    fiesta1 = []
    fiesta2 = []
    for key in colores:
        if colores[key] == 1:
            fiesta1.append(key)
        else:
            fiesta2.append(key)
    return (True, fiesta1, fiesta2)

def dibujarGrafo(grafo, fiesta1, fiesta2):
    G = nx.Graph()
    
    for vertice in grafo:
        G.add_node(vertice)
        for adyacente in grafo[vertice]:
            G.add_edge(vertice, adyacente)
    
    pos = nx.spring_layout(G)
    
    # Colores para los nodos de las dos fiestas
    node_colors = []
    for vertice in G.nodes():
        if vertice in fiesta1:
            node_colors.append('red')
        else:
            node_colors.append('blue')
    
    # Dibujo de nodos y aristas con colores
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    
    plt.show()

def main():
    archivo = sys.argv[1]
    grafo = crearGrafo(leerArchivo(archivo))

    imprimirGrafo(grafo)
    amigos = list(grafo.keys())
    resultado = hayFiesta(grafo, amigos[0])
    if resultado[0]:
        print("SI")
        print("Fiesta 1:", resultado[1])
        print("Fiesta 2:", resultado[2])
        dibujarGrafo(grafo, resultado[1], resultado[2])
    else:
        print("NO")

if __name__ == "__main__":
    main()