from Vertex import Vertex


class Graph:
    def __init__(self, n: int):
        self.n = n
        arr = [n]
        for i in range(0, self.n):
            arr[i] = Vertex(i)
        self.vertices = arr

    def get_vertex(self, i:int):
        return self.vertices[i]

    def add_neighbours(self, v1: Vertex, v2: Vertex):
        v1.add_neighbour(v2.get_index)
        v2.add_neighbour(v1.get_index)
