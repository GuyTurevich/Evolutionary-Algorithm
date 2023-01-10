from RandomGraph import RandomGraph
from CliqueEvaluator import CliqueEvaluator
from CliqueCreator import CliqueCreator
from GraphVisualization import GraphVisualization
from Graph import Graph

class test:


    def bron_kerbosch(graph: Graph) -> str:
        def recurse(r: set, p: set, x: set):
            if not p and not x:
                # found a clique
                nonlocal max_clique
                clique = ''.join(['1' if i in r else '0' for i in range(graph.get_num_vertices())])
                if clique > max_clique:
                    max_clique = clique
            for vertex in p.copy():
                recurse(r | {vertex}, p & set(graph.get_vertex(vertex).get_neighbours()), x & set(graph.get_vertex(vertex).get_neighbours()))
                p.remove(vertex)
                x.add(vertex)
        
        max_clique = ''
        recurse(set(), set(range(graph.get_num_vertices())), set())
        return max_clique


    graph = RandomGraph(8).get_graph()
    evaluator = CliqueEvaluator()
    creator = CliqueCreator()
    individuals = creator.create_individuals(10)
    print (bron_kerbosch(graph))
    GraphVisualization(graph).visualize()
    for individual in individuals:
        GraphVisualization(graph).visualize(individual, evaluator.fitness(individual, graph))

