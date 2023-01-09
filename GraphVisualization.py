import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph

class GraphVisualization:

    G = nx.Graph()

    def __init__(self, graph: Graph):
        self.visual = []
        self.graph = graph
        self.n = graph.get_num_vertices()
          
    
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

    def visualize(self, *args): # 'args' could contain an individual if needed, and 'print' indicates if the graph should be printed or saved
        # create the graph
        num_of_vertices = self.graph.get_num_vertices()
        self.add_nodes(num_of_vertices)
        self.add_edges(self.graph.get_vertices())

        
        
        if len(args) > 0:    # color the nodes if an individual is given
            individual = args[0]
            colors = []
            for i in range(len(individual)):
                if(individual[i] == 1):
                    colors.append('red')
                else:
                    colors.append('gray')
            nx.draw_networkx(self.G, pos = nx.spring_layout(self.G), node_color = colors)
            if len(args) > 1:
                plt.text(0.5, 0.9, "Fitness: " + str(args[1]), ha="center", transform=plt.gcf().transFigure)  # add the fitness value if given
        else:
            nx.draw_networkx(self.G, pos = nx.spring_layout(self.G))
        
        plt.show()
  
