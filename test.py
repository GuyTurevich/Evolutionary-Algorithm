import random
import time
from CliqueCrossover import CliqueCrossover
from CliqueMutation import CliqueMutation
from RandomGraph import RandomGraph
from CliqueEvaluator import CliqueEvaluator
from CliqueCreator import CliqueCreator
from GraphVisualization import GraphVisualization
from Graph import Graph

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator

class test:


    # code we found online that returns the maximum clique in a graph using a known algorithm
    def bron_kerbosch(graph: Graph) -> tuple[int, set[int]]:
        max_size = 0
        max_clique = set()

        def recurse(r, p, x):
            nonlocal max_size, max_clique
            if len(r) > max_size:
                max_size = len(r)
                max_clique = r
            for vertex in p.copy():
                recurse(r | {vertex}, p & set(graph.get_neighbours(vertex)), x & set(graph.get_neighbours(vertex)))
                p.remove(vertex)
                x.add(vertex)

        recurse(set(), set(range(graph.get_num_vertices())), set())
        return max_size, max_clique


    population_size = 200
    random_graph = RandomGraph(100).get_graph()
    GraphVisualization(random_graph).visualize()
    print ("Starting Bron-Kerbosch Algorithm")
    current_time = time.time()
    print (bron_kerbosch(random_graph))
    print("Bron-Kerbosch Algorithm took: ", time.time() - current_time, " seconds")
    algo = SimpleEvolution(
        Subpopulation(creators = GABitStringVectorCreator(length = random_graph.get_num_vertices()),
                      population_size=population_size,
                      # user-defined fitness evaluation method
                      evaluator= CliqueEvaluator(random_graph),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=0.05,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          CliqueCrossover("uniform"),
                          CliqueMutation(1, probability=0.1)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                      ]),
        breeder=SimpleBreeder(),
        max_workers = 4,
        max_generation = 300,
        statistics = BestAverageWorstStatistics()
    )
    print("EA Process Presented Bellow:")

    # evolve the generated initial population
    algo.evolve()
    print("#####################################")

    print("The Ultimate solution found by our solver is:")
    algo.finish()

    


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


