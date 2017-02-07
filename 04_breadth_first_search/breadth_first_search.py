# Breadth-First-Search Algorithm (BFS)
# GJM

import graph
import Queue

def BFS(G, s):
    # BFS(graph.Graph, 1, 6)
    # G: graph instance
    # s: start vertex

    # all nodes initially unexplored - dict of all vertices and their explored status
    vertex_explored = G.vertex_explored_status()

    # dict of vertices and their layer number
    vertex_distances = G.vertex_layer()

    sink_vertex = G.no_vertices

    # mark s as 'explored'
    vertex_explored[s] = True

    # queue stores vertices that have been explored
    Q = Queue.Queue(maxsize=0)
    Q.put(s)
    v = 1   #debugging purposes
    vertex_distances[v] = 0     # initialize first vertex v with distance = 0 (layer 0)

    while not Q.empty():
        # remove first node of Q and call it v.
        # (an edge is (v,w) where v is the vert and w the adj vert)
        v = Q.get()
        if v != sink_vertex:
            for w in G.graph[v]:
                if not vertex_explored[w]:
                    vertex_distances[w] = vertex_distances[v] + 1
                    vertex_explored[w] = True
                    Q.put(w)
    return v

# directed graph text file  (2 columns. col 1 represents current vertex, col 2 represents adjacent vertex)
# (each row represents an edge of the graph)
G = graph.Graph('tiny_graph', 6)
sink_vertex = BFS(G, 1)
