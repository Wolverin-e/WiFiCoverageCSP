from wificoverage.problems import (
    get_small_problem_discrete_eval,
    get_small_problem_less_descrete_eval
)
from algorithms.hillclimbing import (
    HillClimbingRandomRestarts,
    RandomRestartEscapingShoulders
)

problem = get_small_problem_less_descrete_eval()
solver = RandomRestartEscapingShoulders

problem_solver = solver(problem)
problem.show_final_sol(problem_solver.solve())
