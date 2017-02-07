# graph class
# GJM

class Graph:
    # instantiates graph object: dict of vertex-to-adjacent edges(graph), number of vertices
    def __init__(self, edge_lst_txt_file, no_vertices):
        self.no_vertices = no_vertices
        self.graph = self.read_graph_edges(edge_lst_txt_file, no_vertices)


    # takes edge list text file (directed) and returns a dict of vertices (keys) to all adjacent vertices (values)
    def read_graph_edges(self, edge_lst_txt_file, no_vertices):
        with open(edge_lst_txt_file) as f:
            edge_lst = f.readlines()

        # adjacency list: each entry containing list of adjacent vertices
        graph = {k: [] for k in range(1, no_vertices)}
        for row_ind, row in enumerate(edge_lst):
            # convert row of str to row of int
            edge_lst[row_ind] = map(int, row.split())
            # need to append to list of adjacent vertices
            graph[edge_lst[row_ind][0]].append(edge_lst[row_ind][1])

        return graph


    # dict: vertex-to-explored.  keeps record whether or not vertex has been explored
    # (initialized as False -- vertex not explored)
    def vertex_explored_status(self):
        vertices = dict()
        # key: vertex number, value: boolean True of False (explored or unexplored)
        for i in range(1, self.no_vertices+1):
            vertices[i] = False
        return vertices


    # dict: vertex-to-distance.  keeps record of what layer the vertex is on or the distance from starting node
    def vertex_layer(self):
        vertices = dict()
        # key: vertex number, value: vertex distance from start node (or layer number)
        for i in range(1, self.no_vertices+1):
            vertices[i] = 0
        return vertices
