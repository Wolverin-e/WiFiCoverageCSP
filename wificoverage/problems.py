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
        goal_val=8,  # (len(device_coords)+len(initial_wifi_coords)-1)
        device_coords=(
            (2, 2),
            (2, 7),
            (9, 7),
            (9, 5),
            (9, 2)
        ),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5)),
        evaluator=discrete_evaluator
    )


def get_small_problem_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=10,
        grid_width=10,
        wifi_range=2,
        goal_val=0,
        device_coords=(
            (2, 2),
            (2, 7),
            (9, 7),
            (9, 5),
            (9, 2)
        ),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5)),
        evaluator=less_discrete_evaluator
    )


def get_medium_problem6_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=20,
        grid_width=20,
        wifi_range=6,
        goal_val=0,
        device_coords=(
            (2, 2),
            (2, 7),
            (9, 15),
            (14, 10),
            (19, 8),
            (19, 7),
            (10, 17),
            (5, 11),
            (11, 4),
            (4, 15),
            (16, 1),
            (7, 4)
        ),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7)),
        evaluator=less_discrete_evaluator
    )


def get_medium_problem5_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=20,
        grid_width=20,
        wifi_range=5,
        goal_val=0,
        device_coords=(
            (2, 2),
            (2, 7),
            (9, 15),
            (14, 10),
            (19, 8),
            (19, 7),
            (10, 17),
            (5, 11),
            (11, 4),
            (4, 15),
            (16, 1),
            (7, 4)
        ),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5)),
        evaluator=less_discrete_evaluator
    )


def get_medium_problem4_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=20,
        grid_width=20,
        wifi_range=4,
        goal_val=0,
        device_coords=(
            (2, 2),
            (2, 7),
            (9, 15),
            (14, 10),
            (19, 8),
            (19, 7),
            (10, 17),
            (5, 11),
            (11, 4),
            (4, 15),
            (16, 1),
            (7, 4)
        ),
        initial_wifi_coords=((1, 2), (3, 7), (6, 7), (4, 5), (1, 9)),
        evaluator=less_discrete_evaluator
    )


def get_large_problem5_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=35,
        grid_width=35,
        wifi_range=5,
        goal_val=0,
        device_coords=(
            (1, 3),
            (10, 2),
            (15, 1),
            (20, 7),
            (7, 15),
            (15, 17),
            (25, 26),
            (10, 22),
            (30, 13),
            (22, 31),
            (28, 4),
            (5, 28)
        ),
        initial_wifi_coords=(
            (1, 2),
            (3, 7),
            (16, 27),
            (14, 25),
            (16, 19),
            (25, 33),
            (33, 10),
            (22, 3)
        ),
        evaluator=less_discrete_evaluator
    )


def get_large_problem8_less_descrete_eval():
    return WiFiCoverageProblem(
        grid_height=35,
        grid_width=35,
        wifi_range=8,
        goal_val=0,
        device_coords=(
            (1, 3),
            (10, 2),
            (15, 1),
            (20, 7),
            (7, 15),
            (15, 17),
            (25, 26),
            (10, 22),
            (30, 13),
            (22, 31),
            (28, 4),
            (5, 28)
        ),
        initial_wifi_coords=(
            (1, 2),
            (3, 7),
            (16, 27),
            (14, 25)
        ),
        evaluator=less_discrete_evaluator
    )
