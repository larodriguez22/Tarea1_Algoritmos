def read_file():
    global graph
    file_name = input("Inserte el nombre del archivo \n")
    file = open(file_name, "r")
    matrix = file.read()
    vertices = matrix.split("\n")
    graph = [None] * len(vertices)
    for index, vertice in enumerate(vertices):
        if vertice == "-":
            graph[index] = []
        else:
            adjacency_str = vertice.split(" ")
            graph[index] = list(map(lambda x: int(x), adjacency_str))

def dfs(graph):
    global color, parent, discovery, finish, time
    color = ["WHITE"] * len(graph)
    parent = [None] * len(graph)
    discovery = [None] * len(graph)
    finish = [None] * len(graph)
    time = 0
    try:
        for vertex, _ in enumerate(graph):
            if color[vertex] == "WHITE":
                dfs_visit(graph, vertex)
        print("There are no cycles")
    except Exception as message:
        print(str(message))

def dfs_visit(graph, vertex):
    # Time como es primitivo es necesario ponerle global.
    global time
    time = time + 1
    # Discovery como es objeto no es necesario ponerle global.
    discovery[vertex] = time
    color[vertex] = "GREY"
    for neighbour in graph[vertex]:
        match color[neighbour]:
            case "WHITE":
                parent[neighbour] = vertex
                dfs_visit(graph, neighbour) 
            case "GREY":
                raise Exception(f"Has cycle from {vertex} to {neighbour}")
            case _:
                pass
    color[vertex] = "BLACK"
    time = time + 1
    finish[vertex] = time

read_file()
dfs(graph)