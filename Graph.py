

class Graph:
    def __init__(self, num_of_vertices: int):
        self.num_of_vertices = num_of_vertices
        self.adjacency_matrix = [[0 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        
    def add_neighbours(self, v1: int, v2: int):
        self.adjacency_matrix[v1][v2] = 1
        self.adjacency_matrix[v2][v1] = 1
    
    def is_neighbour(self, v1: int, v2: int):
        return self.adjacency_matrix[v1][v2] == 1

    def get_neighbours(self, v: int):
        neighbours = list()
        for i in range(self.num_of_vertices):
            if self.is_neighbour(v, i):
                neighbours.append(i)
        return neighbours

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def get_num_vertices(self):
        return self.num_of_vertices
