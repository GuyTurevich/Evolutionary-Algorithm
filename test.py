import RandomGraph
import CliqueEvaluator
import CliqueCreator
import GraphVisualization

class test:
    graph = RandomGraph.get_graph()
    evaluator = CliqueEvaluator.CliqueEvaluator()
    creator = CliqueCreator.CliqueCreator();
    individuals = creator.create_individuals(10)
    for i in individuals:
        GraphVisualization.GraphVisualization(graph).visualize()
        print(evaluator.fitness(i, graph))