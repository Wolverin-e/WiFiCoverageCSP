class HillClimbingRandomRestarts:

	def __init__(self, problem):
		self.problem = problem

	def solve(self):
		while(True):
			state = self.problem.get_random_state()
			probable_sol = self.solve_util(state)
			self.problem.show_solution(probable_sol)
			if(self.problem.check_constraints(probable_sol)):
				return probable_sol

	def solve_util(self, state):
		current = state # Current Node might be assigned via problem
		neighbour = () # Max valued neighbour

		while(True):
			neighbour = current.get_max_valued_successor()

			if(neighbour.evaluate() <= current.evaluate()):
				return current

			current = neighbour
