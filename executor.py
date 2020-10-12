from wificoverage.problem import WiFiCoverageProblem
from algorithms.hillclimbing.rrhillclimbing import HillClimbingRandomRestarts
from algorithms.hillclimbing.rrescapingshoulders import (
    RandomRestartEscapingShoulders
)

problem = WiFiCoverageProblem(
    grid_height=10,
    grid_width=10,
    wifi_range=2,
    device_coords=((2, 2), (2, 7), (9, 7), (9, 5), (9, 2)),
    initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5))
)

# solver = HillClimbingRandomRestarts(problem)
solver = RandomRestartEscapingShoulders(problem)
problem.show_final_sol(solver.solve())
