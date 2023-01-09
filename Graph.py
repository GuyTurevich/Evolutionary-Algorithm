from Vertex import Vertex


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.vertices = list()
        for i in range(self.n):
            self.vertices.append(Vertex(i))
        

    def get_vertex(self, i:int):
        return self.vertices[i]

    def add_neighbours(self, v1: Vertex, v2: Vertex):
        v1.add_neighbour(v2.get_index)
        v2.add_neighbour(v1.get_index)
