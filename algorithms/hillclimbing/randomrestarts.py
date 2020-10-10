class HillClimbingRandomRestarts:

    def __init__(self, problem):
        self.problem = problem

    def solve(self):
        while(True):
            state = self.problem.get_random_state()
            probable_sol = self.solve_util(state)
            self.problem.show_debug(probable_sol)
            if(self.problem.check_constraints(probable_sol)):
                return probable_sol

    def solve_util(self, state):
        # Current Node might be assigned via problem
        current = state
        neighbour = current.get_max_valued_successor()

        # CHECK IF CURRENT_NODE LOCAL MAXIMA
        while(neighbour.val > current.val):
            current = neighbour
            neighbour = current.get_max_valued_successor()

        return current
