from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from CliqueCreator import CliqueCreator


class CliqueEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

    def fitness(self, individual, graph):
        
        # Create a list to store the cliques in the individual
        cliques = []

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
            
        fitness = 0
        if biggest_clique_size == 0:
            return -(graph.get_num_vertices())

        elif biggest_clique_size > 1:
            fitness = biggest_clique_size
            if len(cliques) == 1:
                fitness += 0.5
        
        for c in cliques:
            if(len(c) == 1): # If the clique is a single vertex, it is not a clique
                fitness -= 1
        
        return fitness