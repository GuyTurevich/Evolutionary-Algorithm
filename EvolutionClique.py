from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.gp_creators.ramped_hh import RampedHalfAndHalfCreator
from eckity.genetic_encodings.gp.tree.functions import f_add, f_mul, f_sub, f_div, \
    f_sqrt, f_log, f_abs, f_max, f_min, f_inv, f_neg
from eckity.genetic_operators.crossovers.subtree_crossover import SubtreeCrossover
from eckity.genetic_operators.mutations.erc_mutation import ERCMutation
from eckity.genetic_operators.mutations.subtree_mutation import SubtreeMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker
from examples.treegp.non_sklearn_mode.symbolic_regression.sym_reg_evaluator import SymbolicRegressionEvaluator

from Graph import Graph
from RandomGraph import RandomGraph
from CliqueCreator import CliqueCreator
from CliqueEvaluator import CliqueEvaluator
from CliqueCrossover import ColoredCrossover
from CliqueMutation import CliqueMutation


algo = SimpleEvolution(
    Subpopulation(creators=CliqueCreator(),
                  population_size=100,
                  evaluator=CliqueEvaluator(),
                  higher_is_better=True,
                  elitism_rate=1/4,
                  operators_sequence=[
        ColoredCrossover(probability=0.8),
        CliqueMutation(probability=0.2)
    ],
        selection_methods=[
        (TournamentSelection(
            tournament_size=3, higher_is_better=True), 1)
    ]
    ),
    breeder=SimpleBreeder(),
    max_workers=4,
    max_generation=100,
    # random_seed=0,
    termination_checker=ThresholdFromTargetTerminationChecker(
        optimal=0, threshold=0.000),
    statistics=BestAverageWorstStatistics()
)

algo.evolve()
