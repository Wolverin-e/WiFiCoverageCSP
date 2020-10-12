class HillClimbing:

    def __init__(self, problem):
        self.problem = problem

    def solve(self, state=None):
        # Current Node might be assigned via problem
        current = state or self.problem.get_initial_state()
        neighbour = current.get_max_valued_successor()

        # CHECK IF CURRENT_NODE LOCAL MAXIMA
        while(neighbour.val > current.val):
            current = neighbour
            neighbour = current.get_max_valued_successor()

        return current
