import random
import time
from CliqueCrossover import CliqueCrossover
from CliqueMutation import CliqueMutation
from RandomGraph import RandomGraph
from CliqueEvaluator import CliqueEvaluator
from GraphVisualization import GraphVisualization
from Graph import Graph

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator


class test:


    num_vertices = 30
    population_size = 120

    random_graph = RandomGraph(num_vertices, 0.5).get_graph()
    graph_visualization = GraphVisualization(random_graph)

    print("Starting NetworkX Algorithm for maximum clique")
    current_time = time.time()
    max_clique = graph_visualization.nx_find_max_clique()
    print((len(max_clique), max_clique))
    print("NetworkX Algorithm took: ", time.time() - current_time, " seconds\n")


    algo = SimpleEvolution(
        Subpopulation(creators=GABitStringVectorCreator(length=random_graph.get_num_vertices()),
                      population_size=population_size,
                      evaluator=CliqueEvaluator(random_graph),
                      higher_is_better=True, # maximization problem
                      elitism_rate=0.05,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          CliqueCrossover("uniform"), # gets - "uniform" or "one_point" or "two_point"
                          CliqueMutation(1, probability=0.1) # gets - (number of bit-flips, probability)
        ],
            selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(
                              tournament_size=4, higher_is_better=True), 1)
        ]),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=50,
        statistics=BestAverageWorstStatistics()
    )
    print("EA Process Presented Bellow:")

    # evolve the generated initial population
    algo.evolve()
    print("#####################################")
    individual = algo.best_of_run_.vector
    graph_visualization.visualize(individual, algo.best_of_run_.get_pure_fitness() )

    print("The Ultimate solution found by our solver is:")
    algo.finish()

