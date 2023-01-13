import random
import time
from RandomGraph import RandomGraph
from CliqueEvaluator import CliqueEvaluator
from CliqueCreator import CliqueCreator
from GraphVisualization import GraphVisualization
from Graph import Graph

class test:


    # code we found online that returns the maximum clique in a graph using a known algorithm
    def bron_kerbosch(graph: Graph) -> tuple[int, set[int]]:
        max_size = 0
        max_clique = set()
        
        def recurse(r: set, p: set, x: set):
            nonlocal max_size, max_clique
            if len(r) > max_size:
                max_size = len(r)
                max_clique = r
            for vertex in p.copy():
                recurse(r | {vertex}, p & set(graph.get_vertex(vertex).get_neighbours()), x & set(graph.get_vertex(vertex).get_neighbours()))
                p.remove(vertex)
                x.add(vertex)

        recurse(set(), set(range(graph.get_num_vertices())), set())
        return max_size, max_clique


    


    # graph = RandomGraph(100).get_graph()
    # print("created graph")
    # evaluator = CliqueEvaluator()
    # creator = CliqueCreator()
    # individuals = creator.create_individuals(5)
    # print("created individuals")
    # print (bron_kerbosch(graph))
    # GraphVisualization(graph).visualize()
   
    # maxfitness = 0
    # individuals_evaluated = 0
    # current_time = time.time()
    # for individual in individuals:
    #     # GraphVisualization(graph).visualize(individual, evaluator.fitness(individual, graph))
    #     # print(evaluator.fitness(individual, graph))
    #     if evaluator.fitness(individual, graph) > maxfitness:
    #         maxfitness = evaluator.fitness(individual, graph)
    #         maxindividual = individual
    #     individuals_evaluated += 1
    #     #if individuals_evaluated % 20000 == 0:
    #     print(str(individuals_evaluated) + " - " + str(maxfitness) + " - " +str(time.time() - current_time))
    # print (maxfitness)
    # print (maxindividual)


