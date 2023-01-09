import numpy as np

class Vertex:
    def __init__(self, index: int):
        self.index = index
        self.neighbours = list()
        


    def get_neighbours(self):
        return self.neighbours

    def get_index(self):
        return self.index

    def add_neighbour(self, i:int):
        self.neighbours.append(i)

    def is_neighbour(self, i:int):
        return i in self.neighbours

    