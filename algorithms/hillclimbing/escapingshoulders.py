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
            if neighbour.val > current.val:
                current = neighbour
                neighbour = current.get_max_valued_successor()
            elif ((neighbour.val == current.val) and
                    (parallel_steps_taken <= allowed_limit)):
                parallel_steps_taken += 1
                neighbour = current.get_max_valued_successor()
            else:
                break

        return current
