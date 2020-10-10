class State:

    # Static Vars
    grid_height = 0
    grid_width = 0
    wifi_range = 0
    device_coords = ()
    direction_vectors = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self, wifi_coords=()):
        self.wifi_coords = wifi_coords
        self.val = self._evaluate()

    def __str__(self):
        state = "WiFi_coords: "+str(self.wifi_coords)+'\n'
        state += "Evaluation: "+str(self.val)
        return state

    def _evaluate(self):
        # DEVICE CHECK & then BFS over WIFI-Coords
        def euclidean(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
        val = 0

        # DEVICES COVERED
        for device in self.device_coords:
            for wifi in self.wifi_coords:
                if(euclidean(device, wifi) <= self.wifi_range):
                    val += 1
                    break

        # WIFI-NETWORK-EVALUATION
        unvisited_nodes = set(self.wifi_coords)

        def get_neighbours(a): return [
            x for x in unvisited_nodes if euclidean(x, a) <= 2*self.wifi_range]

        def bfs(start_node):
            visited = set()
            processing_queue = [start_node]

            while(processing_queue):
                current_processing_node = processing_queue.pop(0)
                visited.add(current_processing_node)

                for neigbour in get_neighbours(current_processing_node):
                    if(neigbour not in visited and
                            neigbour not in processing_queue):
                        processing_queue.append(neigbour)

            return visited

        while unvisited_nodes:
            visited = bfs(next(iter(unvisited_nodes)))
            unvisited_nodes.difference_update(visited)

            if(len(visited) > 1):
                val += len(visited)-1
            else:
                assert(len(visited) == 1)

        return val

    def get_max_valued_successor(self):
        # Check out all the combitions: |wifi_coords|^|direction_vectors|

        def get_sum(a, b):
            return (a[0]+b[0], a[1]+b[1])

        def is_in_grid(coord):
            return not (coord[0] >= self.grid_width or coord[0] < 0 or
                        coord[1] >= self.grid_height or coord[1] < 0)

        max_val = -1
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
