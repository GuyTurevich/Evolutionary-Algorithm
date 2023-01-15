import random
from Graph import Graph

class RandomGraph:

    def __init__(self,num_of_vertices : int, probability : float):

        self.num_of_vertices = num_of_vertices
        self.inputGraph = Graph(num_of_vertices)
        for i in range(num_of_vertices):
            for j in range(i+1,num_of_vertices):
                if random.uniform(0,1) <= probability:              # add edge with given probability
                    self.inputGraph.add_neighbours(i , j)
  

    def get_graph(self):
        return self.inputGraph

