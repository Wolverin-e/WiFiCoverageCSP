def discrete_evaluator(state):
    # DEVICE CHECK & then BFS over WIFI-Coords
    def euclidean(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    val = 0

    # DEVICES COVERED
    for device in state.device_coords:
        for wifi in state.wifi_coords:
            if(euclidean(device, wifi) <= state.wifi_range):
                val += 1
                break

    # WIFI-NETWORK-EVALUATION
    unvisited_nodes = set(state.wifi_coords)

    def get_neighbours(a):
        return [
            x for x in unvisited_nodes if euclidean(x, a) <= 2*state.wifi_range
        ]

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


def less_discrete_evaluator(state):
    # DEVICE CHECK & then BFS over WIFI-Coords
    def euclidean(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    val = 0

    # DEVICES COVERED
    for device in state.device_coords:
        min_dist = float('inf')
        for wifi in state.wifi_coords:
            dist = euclidean(device, wifi)
            if(dist <= state.wifi_range):
                min_dist = 0
                break
            elif(dist < min_dist):
                min_dist = dist
        val += min_dist-state.wifi_range if min_dist else 0

    # WIFI-NETWORK-EVALUATION
    unvisited_nodes = set(state.wifi_coords)

    def get_neighbours(a):
        return [
            x for x in unvisited_nodes if euclidean(x, a) <= 2*state.wifi_range
        ]

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

    def get_mid_estimate(disconnected_component):
        if not disconnected_component:
            return None
        a = 0
        b = 0
        for x, y in disconnected_component:
            a += x
            b += y

        no_of_coords = len(disconnected_component)
        return (a/no_of_coords, b/no_of_coords)

    previous_disconnected_comp_cen = None
    while unvisited_nodes:
        visited = bfs(next(iter(unvisited_nodes)))
        unvisited_nodes.difference_update(visited)
        if not previous_disconnected_comp_cen:
            previous_disconnected_comp_cen = get_mid_estimate(visited)
        elif previous_disconnected_comp_cen:
            next_disconnected_comp = get_mid_estimate(visited)
            val += euclidean(
                previous_disconnected_comp_cen,
                next_disconnected_comp
            )
            previous_disconnected_comp_cen = next_disconnected_comp

    return -val
