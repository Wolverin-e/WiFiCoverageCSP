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
		return random.randint(0, 100)

	def get_max_valued_successor(self):
		# Check out all the combitions
		# |wifi_coords|^|direction_vectors|

		max_val = -1
		max_state = ()


		get_sum = lambda a, b: (a[0]+b[0], a[1]+b[1])
		depth_limit = len(self.wifi_coords)-1

		def go_recursive(depth=0, directions_vector=[]):
			print(directions_vector)
			nonlocal max_val
			nonlocal max_state
			if depth==depth_limit:
				for dir_vec in self.direction_vectors:
					directions_vector.append(dir_vec)
					print(directions_vector)

					state = tuple([get_sum(a, b) for (a, b) in zip(directions_vector, self.wifi_coords)])
					
					print(state)
					end_state = State(state)
					end_state_eval = end_state.evaluate()
					if(end_state_eval > max_val):
						max_val = end_state_eval
						max_state = end_state

					directions_vector.pop()
			else:
				for dir_vec in self.direction_vectors:
					directions_vector.append(dir_vec)
					go_recursive(depth+1, directions_vector)
					directions_vector.pop()

		go_recursive(depth=0, directions_vector=[])
		return max_state

