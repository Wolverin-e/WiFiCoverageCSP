from .evaluator import less_discrete_evaluator


class State:

    # Static Vars
    grid_height = 0
    grid_width = 0
    wifi_range = 0
    device_coords = ()
    evaluator = less_discrete_evaluator
    direction_vectors = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self, wifi_coords=()):
        self.wifi_coords = wifi_coords
        self.val = self.evaluator()

    def __str__(self):
        state_str = "WiFi_coords: "+str(self.wifi_coords)+'\n'
        state_str += "Evaluation: "+str(self.val)
        return state_str

    def get_max_valued_successor(self):
        # Check out all the combitions: |wifi_coords|^|direction_vectors|

        def get_sum(a, b):
            return (a[0]+b[0], a[1]+b[1])

        def is_in_grid(coord):
            return not (coord[0] >= self.grid_width or coord[0] < 0 or
                        coord[1] >= self.grid_height or coord[1] < 0)

        max_val = -float('inf')
        max_state = State()
        depth_limit = len(self.wifi_coords)
        assert(depth_limit > 0)

        def go_recursive(depth=0, partial_state=[]):
            nonlocal max_val
            nonlocal max_state

            if depth == depth_limit:
                new_wifi_coords = tuple(partial_state)
                end_state = State(new_wifi_coords)
                if(end_state.val >= max_val):
                    max_val = end_state.val
                    max_state = end_state
            else:
                for dir_vec in self.direction_vectors:
                    next_vec = get_sum(dir_vec, self.wifi_coords[depth])
                    if (is_in_grid(next_vec) and
                            (next_vec not in partial_state)):
                        partial_state.append(next_vec)
                        go_recursive(depth+1, partial_state)
                        partial_state.pop()

        go_recursive()
        return max_state
