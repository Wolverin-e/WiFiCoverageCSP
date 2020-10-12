from .problem import WiFiCoverageProblem
from .evaluator import (
    discrete_evaluator,
    less_discrete_evaluator
)


def get_small_problem_discrete_eval():
    return WiFiCoverageProblem(
        grid_height=10,
        grid_width=10,
        wifi_range=2,
        device_coords=((2, 2), (2, 7), (9, 7), (9, 5), (9, 2)),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5)),
        evaluator=discrete_evaluator
    )


def get_small_problem_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=10,
        grid_width=10,
        wifi_range=2,
        goal_val=-1,
        device_coords=((2, 2), (2, 7), (9, 7), (9, 5), (9, 2)),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5)),
        evaluator=less_discrete_evaluator
    )
