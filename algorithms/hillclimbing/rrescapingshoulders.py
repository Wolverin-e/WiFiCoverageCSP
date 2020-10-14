from .escapingshoulders import HillClimbingEscapingShoulders


class RandomRestartEscapingShoulders:

    def __init__(self, problem):
        self.problem = problem
        self.esc_shoulder_solver = HillClimbingEscapingShoulders(problem)

    def solve(self):
        # self.problem.show_problem(show_graph=True)
        while(True):
            random_state = self.problem.get_random_state()
            probable_solution = self.esc_shoulder_solver.solve(
                random_state,
                limit=3
            )
            self.problem.show_debug(probable_solution, show_graph=True)
            if self.problem.check_constraints(probable_solution):
                return probable_solution
