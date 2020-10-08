from wificoverage.problem import WiFiCoverageProblem
from algorithms.hillclimbing.randomrestarts import HillClimbingRandomRestarts

problem = WiFiCoverageProblem(
	grid_height=10,
	grid_width=10,
	wifi_range=3,
	goal_val=7,
	device_coords=((2, 2), (3, 3), (5, 5)),
	initial_wifi_coords=((1, 2), (3, 7))
)
# WiFi count

# print(problem.get_initial_state().get_max_valued_successor())

solver = HillClimbingRandomRestarts(problem)
problem.show_solution(solver.solve())
