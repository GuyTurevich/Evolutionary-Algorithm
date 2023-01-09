from RandomGraph import RandomGraph
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange


class ColoredCrossover(GeneticOperator):
    def __init__(self, probability=1, arity=2, events=None):
        super().__init__(probability, arity, events)

    def apply(self, individuals):
        n = RandomGraph.get_n_vertices
        cross1 = [n]
        cross2 = [n]
        clique_father = individuals[1]
        for i in range(n):
            if i < n/2:
                cross1[i] = individuals[0][i]
                cross2[i] = individuals[1][i]
            else:
                cross1[i] = individuals[1][i]
                cross2[i] = individuals[0][i]
        individuals[0] = cross1
        individuals[1] = cross2
        return individuals
