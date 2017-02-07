# Depth-First-Search Algorithm (DFS)
# Recursive implementation
# Computes topological ordering of directed acyclic graph using DFS
# GJM

import graph

def DFS_recursive(G, s):
    # DFS_recursive(graph.Graph, 1)
    # G: graph instance
    # s: start vertex

    sink_vertex = G.no_vertices

    # mark s as 'explored'
    G.vertices_explored[s] = True

    # stack stores vertices that have been explored
    stack = list()
    stack.append(s)
    v = 1
    G.vertex_layers[v] = 0     # initialize first vertex v with distance = 0 (layer 0)

    while stack:
        # remove first node of Q and call it v.
        # (an edge is (v,w) where v is the vert and w the adj vert)
        v = stack.pop()
        if v != sink_vertex:
            for w in G.graph[v]:
                if not G.vertices_explored[w]:
                    G.vertex_layers[w] = G.vertex_layers[v] + 1
                    G.vertices_explored[w] = True
                    DFS_recursive(G, w)

    return v

# directed graph text file  (2 columns. col 1 represents current vertex, col 2 represents adjacent vertex)
# (each row represents an edge of the graph)
G = graph.Graph('tiny_graph', 6)

# all nodes initially unexplored - dict of all vertices and their explored status
G.vertex_explored_status()

# dict of vertices and their layer number
G.vertex_layer()

DFS_recursive(G, 1)
a=1
