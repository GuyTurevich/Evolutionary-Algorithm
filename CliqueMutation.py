from eckity.genetic_operators.genetic_operator import GeneticOperator
import random

class CliqueMutation(GeneticOperator): # Gets the number of bit flips - the number of indexes to mutate in the individual
    def __init__(self, num_bit_flips, probability=0.05, arity=1, events=None):
        super().__init__(probability, 1, events)
        self.num_bit_flips = num_bit_flips

    def apply(self, individuals):
        for individual in individuals:
            random_bits = [random.randint(0, len(individual)-1) for i in range(self.num_bit_flips)] # generate random indexes to mutate
            for random_bit in random_bits:
                individual[random_bit] = 1 if individual[random_bit] == 0 else 0
        self.applied_individuals = individuals
        return individuals

            

