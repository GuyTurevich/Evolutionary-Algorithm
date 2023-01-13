from eckity.creators.creator import Creator
from RandomGraph import RandomGraph
import random


class CliqueCreator(Creator):
    def __init__(self, events=None):
        super().__init__(events)

    def create_individuals(self, n_individuals, higher_is_better=True):
        population = []
        for i in range(n_individuals):
            individual = []
            for j in range(RandomGraph.get_instance().num_of_vertices):
                individual.append(random.randint(0, 1))
            population.append(individual)
        self.created_individuals = population
        return population


