import random
from RandomGraph import RandomGraph
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange


class CliqueCrossover(GeneticOperator): 
    def __init__(self, crossover_type, probability=0.8, arity=2, events=None): # gets one of the following crossover types - 
        super().__init__(probability=probability, arity=arity, events=events)  # one_point, two_point, uniform
        self.crossover_type = crossover_type

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if (i+1<len(individuals)):
                individual1 = individuals[i].get_vector()
                individual2 = individuals[i+1].get_vector()
                if(self.crossover_type == "one_point"):
                    individual1, individual2 = self.one_point(individual1, individual2)
                elif(self.crossover_type == "two_point"):
                    individual1, individual2 = self.two_point(individual1, individual2)
                elif(self.crossover_type == "uniform"):
                    individual1, individual2 = self.uniform(individual1, individual2)
                individuals[i].set_vector(individual1)
                individuals[i+1].set_vector(individual2)
        self.applied_individuals = individuals
        return individuals
        
    # swap the values from an index to the end of the list 
    def one_point(self, individual1, individual2):
        index = randrange(0, len(individual1))
        for i in range(index, len(individual1)): 
            individual1[i], individual2[i] = individual2[i], individual1[i]
        return individual1, individual2 

    # swap the values between two indexes
    def two_point(self, individual1, individual2):
        index1, index2 = sorted(random.sample(range(len(individual1)), 2)) # randomly select two indexes and make sure that index1 < index2 
        for i in range(index1, index2):
            individual1[i], individual2[i] = individual2[i], individual1[i] 
        return individual1, individual2
    
    # swap each value with a 50% chance
    def uniform(self, individual1, individual2):
        for i in range(len(individual1)):
            if random.random() < 0.5:
                individual1[i], individual2[i] = individual2[i], individual1[i] 
        return individual1, individual2
    
    