from Vertex import Vertex


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.vertices = list()
        for i in range(self.n):
            self.vertices.append(Vertex(i))
        

    def get_vertex(self, i:int):
        return self.vertices[i]

    def get_vertices(self):
        return self.vertices

    def add_neighbours(self, v1: int, v2: int):
        self.get_vertex(v1).add_neighbour(v2)
        self.get_vertex(v2).add_neighbour(v1)

    def get_num_vertices(self):
        return self.n