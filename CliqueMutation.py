from eckity.genetic_operators.genetic_operator import GeneticOperator
import random

class CliqueMutation(GeneticOperator):
    def __init__(self, probability=1, arity=1, events=None):
        super().__init__(probability, 1, events)

    def apply(self, individuals):
        vertex_mutation_rate = 0.05
        clique = individuals[0]
        for i in clique:
            probability = random.random
            if probability < vertex_mutation_rate:
                if clique[i] == 0:
                    clique[i] == 1
                else: clique[i] == 0
        individuals[0] = clique
        return individuals

            

