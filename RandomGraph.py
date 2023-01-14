import random
from Graph import Graph

class RandomGraph:
    __instance = None  #singleton instance


    def __init__(self,num_of_vertices : int, probability : float):
        if RandomGraph.__instance != None:
            return self.__instance
        else:
            self.num_of_vertices = num_of_vertices
            self.inputGraph = Graph(num_of_vertices)
            for i in range(num_of_vertices):
                for j in range(i+1,num_of_vertices):
                    if random.uniform(0,1) <= probability:              # add edge with given probability
                        self.inputGraph.add_neighbours(i , j)
            RandomGraph.__instance = self                       # singleton instance created

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            raise Exception("Singleton was not created, use constructor")
        return cls.__instance

    def get_graph(self):
        return self.inputGraph

