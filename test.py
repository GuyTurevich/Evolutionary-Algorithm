from RandomGraph import RandomGraph
from CliqueEvaluator import CliqueEvaluator
from CliqueCreator import CliqueCreator
from GraphVisualization import GraphVisualization

class test:
    graph = RandomGraph(12).get_graph()
    evaluator = CliqueEvaluator()
    creator = CliqueCreator()
    individuals = creator.create_individuals(5)
    GraphVisualization(graph).visualize()
    for individual in individuals:
        GraphVisualization(graph).visualize(individual, evaluator.fitness(individual, graph))