class HillClimbingEscapingShoulders:

    def __init__(self, problem):
        self.problem = problem

    def solve(self, state=None, limit=None):
        # Current Node might be assigned via problem
        current = state or self.problem.get_initial_state()
        neighbour = current.get_max_valued_successor()
        allowed_limit = limit or 100

        # CHECK IF CURRENT_NODE LOCAL MAXIMA
        parallel_steps_taken = 0
        while(True):
            self.problem.show_debug(current, show_graph=True, sleep=0.01)
            if neighbour.val > current.val:
                parallel_steps_taken = 0
                current = neighbour
                neighbour = current.get_max_valued_successor()
            elif self.problem.check_constraints(current):
                break
            elif ((neighbour.val == current.val) and
                    (parallel_steps_taken <= allowed_limit)):
                parallel_steps_taken += 1
                neighbour = current.get_max_valued_successor()
            else:
                break

        return current
