from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from CliqueCreator import CliqueCreator


class CliqueEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

    def fitness(self, individual, graph):
        
        biggest_clique_size = 0
        redundant_vertices_count = 0
        num_of_ones = 0

        for i in range(len(individual)):
            if individual[i] == 1:

                num_of_ones += 1
                cliques = []
                is_redudant = True
                
                # adds a clique for each vertex the vertex 'i' is connected to
                # create new clique only for vertices with a bigger index than 'i'
                # increment redundant_vertices_count if the vertex 'i' is not connected to any other vertex
                for j in range(len(individual)):
                    if individual[j] == 1 and graph.get_vertex(i).is_neighbour(j):
                        is_redudant = False
                        if j > i:
                            cliques.append({i, j})
                if is_redudant:
                    redundant_vertices_count += 1

                # for each clique in the list, add all vertices that are connected to all vertices in the clique
                for c in cliques:
                    for j in range(i+1, len(individual)):
                        if individual[j] == 1 and all([graph.get_vertex(j).is_neighbour(k) for k in c]):
                            c.add(j)
                
                # update biggest_clique_size if needed
                if len(cliques) > 0:
                    biggest_clique_size = max(biggest_clique_size, max([len(c) for c in cliques]))

        # add a 0.5 bonus if the individual represents a clique perfectly
        return biggest_clique_size + (0.5 if biggest_clique_size == num_of_ones else 0) - redundant_vertices_count
        