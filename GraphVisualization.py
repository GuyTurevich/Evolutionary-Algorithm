import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph

class GraphVisualization:

    G = nx.Graph()

    def __init__(self, graph: Graph):
        self.visual = []
        self.graph = graph
        self.n = graph.get_num_vertices()
        self.add_nodes(self.n)
        self.add_edges(self.graph.get_adjacency_matrix())
          
    
    def add_nodes(self, n):
        for i in range(n):
            self.G.add_node(i)

    def add_edges(self, adjacency_matrix):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if adjacency_matrix[i][j] == 1:
                    self.visual.append((i, j))
        self.G.add_edges_from(self.visual)
    
    def nx_find_max_clique(self):
        cliques = list(nx.find_cliques(self.G))
        max_clique = max(cliques, key=len)
        return max_clique

    def visualize(self, *args): # 'args' could contain an individual and its fitness value
        
        if len(args) > 0:    # color the nodes if an individual is given
            individual = args[0]
            colors = []
            for i in range(len(individual)):
                if(individual[i] == 1):
                    colors.append('red')
                else:
                    colors.append('gray')
            nx.draw_networkx(self.G, pos = nx.spring_layout(self.G), width = 0.15, node_color = colors)
            if len(args) > 1:
                plt.text(0.5, 0.9, "Fitness: " + str(args[1]), ha="center", transform=plt.gcf().transFigure)  # add the fitness value if given
        else:
            nx.draw_networkx(self.G, pos = nx.spring_layout(self.G), width = 0.15, node_size = 70, font_size = 6)
        
        plt.savefig("graph.png", dpi = 600)
  
