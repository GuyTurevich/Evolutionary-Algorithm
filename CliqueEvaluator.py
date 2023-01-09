from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from CliqueCreator import CliqueCreator


class CliqueEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

def fitness(individual, graph):
    clique_count = 0
    clique_size = 0
    
    # Create a list to store the cliques in the individual
    cliques = []
    
    # Create a list to store the vertices that have been included in a clique
    currentClique = []

    biggest_clique_size = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            is_in_clique = False
            for c in cliques:
                if all([graph.get_vertex(i).is_neighbour(j) for j in c]):
                    c.append(i)
                    is_in_clique = True
                    biggest_clique_size = max(biggest_clique_size, len(c))

            if not is_in_clique:
                currentClique = [i]
                cliques.append(currentClique)
                biggest_clique_size = max(biggest_clique_size, len(currentClique))
        
    # Calculate the fitness of the individual based on the size of the cliques and the number of 1's that don't belong to any clique
    fitness = 0
    for c in cliques:
        if(len(c) == 1): # If the clique is a single vertex, it is not a clique
            fitness -= 1
        elif len(c) != biggest_clique_size: 
            fitness += len(c)
        else:
            fitness += len(c) ** 2 # If the clique is the biggest clique, give it a higher fitness value
    
    return fitness