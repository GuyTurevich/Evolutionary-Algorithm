from RandomGraph import RandomGraph
import time
from CliqueCrossover import CliqueCrossover
from CliqueMutation import CliqueMutation
from CliqueEvaluator import CliqueEvaluator
from GraphVisualization import GraphVisualization
from Graph import Graph

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator


class EvolutionaryAlgorithm:

    def __init__(self, graph_size, edge_prob, population_size, elitism_rate, mutation_prob, mutation_bit_flips, tournament_size, tournament_prob, crossover_type, max_generation):
        
        self.graph = RandomGraph(graph_size, edge_prob).get_graph()
        self.edge_prob = edge_prob
        self.population_size = population_size
        self.crossover_type = crossover_type
        self.elitism_rate = elitism_rate
        self.mutation_probability = mutation_prob
        self.mutation_bit_flips = mutation_bit_flips
        self.tournament_size = tournament_size
        self.tournament_probability = tournament_prob
        self.max_generation = max_generation
        self.num_vertices = self.graph.get_num_vertices()
        self.graph_visualization = GraphVisualization(self.graph)

    def run(self):
        self.before_run()
        start_time = time.time()
        algo = SimpleEvolution(
            Subpopulation(creators=GABitStringVectorCreator(self.num_vertices),
                          population_size=self.population_size,
                          evaluator=CliqueEvaluator(self.graph),
                          higher_is_better=True,  # maximization problem
                          elitism_rate=self.elitism_rate,
                          # genetic operators sequence to be applied in each generation
                          operators_sequence=[
                          # gets - "uniform" or "one_point" or "two_point"
                          CliqueCrossover(self.crossover_type),
                          # gets - (number of bit-flips, probability)
                          CliqueMutation(self.mutation_bit_flips, self.mutation_probability),
            ],
                selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(
                    tournament_size=self.tournament_size, higher_is_better=True), self.tournament_probability)
            ]),
            breeder=SimpleBreeder(),
            max_workers=4,
            max_generation= self.max_generation,
            statistics=BestAverageWorstStatistics()
        )
    


        algo.evolve()
        print("#####################################")
        print("Total Time: ", f'{(time.time() - start_time):.2f}', " seconds")

        individual = algo.best_of_run_.vector
        self.graph_visualization.visualize(
            individual, algo.best_of_run_.get_pure_fitness())


    def before_run(self):
        print("Starting NetworkX Algorithm for maximum clique")
        max_clique = self.graph_visualization.nx_find_max_clique()
        print((len(max_clique), max_clique))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("Running Evolutionary Algorithm")
        print("Graph Size: " + str(self.num_vertices))
        print("Graph Edge Probability: " + str(self.edge_prob))
        print("Population Size: " + str(self.population_size))
        print("Elitism Rate: " + str(self.elitism_rate))
        print("Mutation Probability: " + str(self.mutation_probability))
        print("Mutation Bit Flips: " + str(self.mutation_bit_flips))
        print("Tournament Size: " + str(self.tournament_size))
        print("Tournament Probability: " + str(self.tournament_probability))
        print("Crossover Type: " + str(self.crossover_type))
        print("Max Generation: " + str(self.max_generation))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")