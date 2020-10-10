from wificoverage.problem import WiFiCoverageProblem
from algorithms.hillclimbing.randomrestarts import HillClimbingRandomRestarts

problem = WiFiCoverageProblem(
	grid_height=10,
	grid_width=10,
	wifi_range=2,
	goal_val=8,
	device_coords=((2, 2), (2, 7), (9, 7), (9, 5), (7, 2)),
	initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5))
)
# WiFi count

# print(problem.get_initial_state().get_max_valued_successor())

solver = HillClimbingRandomRestarts(problem)
problem.show_final_sol(solver.solve())
