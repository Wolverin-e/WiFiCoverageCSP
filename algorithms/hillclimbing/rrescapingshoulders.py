from .escapingshoulders import HillClimbingEscapingShoulders


class RandomRestartEscapingShoulders:

    def __init__(self, problem):
        self.problem = problem
        self.esc_shoulder_solver = HillClimbingEscapingShoulders(problem)

    def solve(self):
        while(True):
            random_state = self.problem.get_random_state()
            probable_solution = self.esc_shoulder_solver.solve(
                random_state,
                limit=20
            )
            self.problem.show_debug(probable_solution)
            if self.problem.check_constraints(probable_solution):
                return probable_solution
