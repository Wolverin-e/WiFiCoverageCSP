from .state import State
import random
import matplotlib.pyplot as plt


class WiFiCoverageProblem():

    def __init__(self, grid_height=0, grid_width=0, wifi_range=0,
                 device_coords=(), initial_wifi_coords=()):
        State.grid_height = grid_height
        State.grid_width = grid_width
        State.wifi_range = wifi_range
        State.device_coords = device_coords

        self.grid_height = grid_height
        self.grid_width = grid_width
        self.wifi_range = wifi_range
        self.goal_val = len(device_coords)+len(initial_wifi_coords)-1
        self.device_coords = device_coords
        self.initial_state = State(wifi_coords=initial_wifi_coords)

    def get_initial_state(self):
        return self.initial_state

    def check_constraints(self, state=State()):
        return (state.val >= self.goal_val)

    def get_random_state(self):
        state = []
        for i in range(len(self.initial_state.wifi_coords)):
            state.append((
                random.randrange(0, self.grid_width),
                random.randrange(0, self.grid_height)
            ))
        return State(tuple(state))

    def _show_grid_in_terminal(self, state=State()):
        grid = [
            [' ' for x in range(self.grid_width)]
            for y in range(self.grid_height)
        ]

        print(state)
        for x, y in state.wifi_coords:
            grid[x][y] = 'X'

        for x, y in self.device_coords:
            grid[x][y] = '*'

        for y in range(self.grid_height-1, -1, -1):
            print("|", end="")
            for x in range(self.grid_width):
                print(grid[x][y], end="")
            print("|")

        print()

    def _show_graph(self, state=State(), pause=None):
        plt.cla()
        x, y = zip(*self.device_coords)
        plt.plot(x, y, 'ro')
        x, y = zip(*state.wifi_coords)
        plt.plot(x, y, 'b^')
        plt.axis([0, 10, 0, 10])

        ax = plt.gca()
        for coord in state.wifi_coords:
            circle = plt.Circle(coord, self.wifi_range, color='g', fill=False)
            ax.add_artist(circle)
            ax.set_aspect('equal', 'box')

        if(pause is not None):
            plt.show(block=False)
            plt.pause(0.5)
        else:
            plt.show()

    def show_debug(self, debug_state):
        self._show_grid_in_terminal(debug_state)
        # self._show_graph(debug_state, 0.25)

    def show_final_sol(self, solution_state):
        self._show_graph(solution_state)
