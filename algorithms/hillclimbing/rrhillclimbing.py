from .hillclimbing import HillClimbing


class HillClimbingRandomRestarts:

    def __init__(self, problem):
        self.problem = problem
        self.hill_climbing_solver = HillClimbing(problem)

    def solve(self):
        while(True):
            random_state = self.problem.get_random_state()
            probable_sol = self.hill_climbing_solver.solve(random_state)
            self.problem.show_debug(probable_sol)
            if(self.problem.check_constraints(probable_sol)):
                return probable_sol
