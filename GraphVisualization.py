import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph

class GraphVisualization:

    G = nx.Graph()

    def __init__(self, *graph: Graph):
        self.visual = []
        self.graph = graph
          
    
    def add_nodes(self, n):
        for i in range(n):
            self.G.add_node(i)

    def add_edges(self, vertices: list):
        for vertex in vertices:
            for neighbour in vertex.get_neighbours():
                temp = [vertex.get_index(), neighbour]
                reverse_temp = [neighbour, vertex.get_index()]
                if(temp not in self.visual and reverse_temp not in self.visual):
                    self.visual.append(temp)
        self.G.add_edges_from(self.visual)

          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        self.G.add_nodes(len(self.graph.get_vertices()))
        self.G.add_edges(self.graph.get_vertices())
        nx.draw_networkx(self.G)
        plt.show()
  
