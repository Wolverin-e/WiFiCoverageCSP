from copy import deepcopy
import random

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

	def __str__(self):
		state = "WiFi_coords: "+str(self.wifi_coords)
		return state

	def clone(self):
		return State(deepcopy(self.wifi_coords))

	def evaluate(self):
		# BFS over WIFI-Coords & then DEVICE CHECK
		# return random.randint(0, 100)

		euclidean = lambda a, b: ( (a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5

		val = 0
		#device check
		for device in self.device_coords:
			for wifi in self.wifi_coords:
				if(euclidean(device, wifi) <= self.wifi_range):
					val+=1
					break

		unvisited_nodes = set(self.wifi_coords)
		get_neighbours = lambda a: [x for x in unvisited_nodes if euclidean(x, a)<=2*self.wifi_range]

		def bfs(start_node):
			visited = set()
			processing_queue = [start_node]

			while(processing_queue):
				current_processing_node = processing_queue.pop(0)
				visited.add(current_processing_node)

				for neigbour in get_neighbours(current_processing_node):
					if (neigbour not in visited) and (neigbour not in processing_queue):
						processing_queue.append(neigbour)

			return visited

		while unvisited_nodes:
			visited = bfs(next(iter(unvisited_nodes)))
			unvisited_nodes.difference_update(visited)

			if(len(visited)>1):
				val+=len(visited)-1
			else:
				assert(len(visited) == 1)

		return val


	def get_max_valued_successor(self):
		# Check out all the combitions
		# |wifi_coords|^|direction_vectors|
		# print("CALLED OF", self)

		max_val = -1
		max_state = State()


		get_sum = lambda a, b: (a[0]+b[0], a[1]+b[1])
		depth_limit = len(self.wifi_coords)-1
		assert(depth_limit>0)

		def go_recursive(depth=0, directions_vector=[]):
			nonlocal max_val
			nonlocal max_state
			if depth==depth_limit:
				for dir_vec in self.direction_vectors:
					directions_vector.append(dir_vec)

					new_wifi_coords = tuple([get_sum(a, b) for (a, b) in zip(directions_vector, self.wifi_coords)])

					flag = 0
					for x, y in new_wifi_coords:
						if(x>=self.grid_width or x<0 or y>=self.grid_height or y<0):
							# print(directions_vector)
							flag = 1

					if (not flag & len(set(new_wifi_coords)) < len(new_wifi_coords)):
						print("Detected:", new_wifi_coords)
						flag = 1

					if(not flag):
						end_state = State(new_wifi_coords)
						end_state_eval = end_state.evaluate()
						# print(end_state, end_state_eval)
						if(end_state_eval >= max_val):
							max_val = end_state_eval
							max_state = end_state

					directions_vector.pop()
			else:
				for dir_vec in self.direction_vectors:
					directions_vector.append(dir_vec)
					go_recursive(depth+1, directions_vector)
					directions_vector.pop()

		go_recursive()
		return max_state

