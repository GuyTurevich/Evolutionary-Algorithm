import random
from Graph import Graph

class RandomGraph:
    numOfVertices = 20
    inputGraph = Graph(numOfVertices)
    for i in range(numOfVertices):
        for j in range(i+1,numOfVertices):
            if random.uniform(0,1) >= 0.3:    # 70% chance of being connected
                inputGraph.add_neighbours(i , j)

    def get_graph(self):
        return self.inputGraph

