# Breadth-First-Search Algorithm (BFS)
# Performs BFS to compute shortest path
# GJM

import graph
import Queue

def BFS(G, s):
    # BFS(graph.Graph, 1)
    # G: graph instance
    # s: start vertex

    sink_vertex = G.no_vertices

    # mark s as 'explored'
    G.vertices_explored[s] = True

    # queue stores vertices that have been explored
    Q = Queue.Queue(maxsize=0)
    Q.put(s)
    v = 1
    G.vertex_layers[v] = 0     # initialize first vertex v with distance = 0 (layer 0)

    while not Q.empty():
        # remove first node of Q and call it v.
        # (an edge is (v,w) where v is the vert and w the adj vert)
        v = Q.get()
        if v != sink_vertex:
            for w in G.graph[v]:
                if not G.vertices_explored[w]:
                    G.vertex_layers[w] = G.vertex_layers[v] + 1
                    G.vertices_explored[w] = True
                    Q.put(w)
    return v

# directed graph text file  (2 columns. col 1 represents current vertex, col 2 represents adjacent vertex)
# (each row represents an edge of the graph)
G = graph.Graph('tiny_graph', 6)

# all nodes initially unexplored - dict of all vertices and their explored status
G.vertex_explored_status()

# dict of vertices and their layer number
G.vertex_layer()

sink_vertex = BFS(G, 1)
a=1
