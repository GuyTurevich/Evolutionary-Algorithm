from eckity.termination_checkers.termination_checker import TerminationChecker

class TerminationCheckerChange(TerminationChecker):

    def __init__(self, num_generations, higher_is_better=True):
        super().__init__()
        self.higher_is_better = higher_is_better
        self.highest_fitness = 0
        self.unchanged_generations = 0
        self.num_generations = num_generations
    
    def should_terminate(self, population, best_individual, gen_number):
        if self.highest_fitness < best_individual.get_pure_fitness():
            self.highest_fitness = best_individual.get_pure_fitness()
            self.unchanged_generations = 0
        else:
            self.unchanged_generations += 1
        if self.unchanged_generations == self.num_generations:
            return True
        return False