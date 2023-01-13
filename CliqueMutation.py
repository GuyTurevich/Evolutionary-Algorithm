from eckity.genetic_operators.genetic_operator import GeneticOperator
import random

class CliqueMutation(GeneticOperator): # Gets the number of bit flips - the number of indexes to mutate in the individual
    def __init__(self, num_bit_flips, probability=0.05, arity=1, events=None):
        super().__init__(probability, 1, events)
        self.num_bit_flips = num_bit_flips

    def apply(self, individuals):
        for individual in individuals:
            individual_vector = individual.get_vector()
            random_bits = [random.randint(0, len(individual_vector)-1) for i in range(self.num_bit_flips)] # generate random indexes to mutate
            for random_bit in random_bits:
                individual_vector[random_bit] = 1 if individual_vector[random_bit] == 0 else 0
            individual.set_vector(individual_vector)
        self.applied_individuals = individuals
        return individuals

            

