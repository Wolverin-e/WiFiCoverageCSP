from .state import State
import random
import matplotlib.pyplot as plt

class WiFiCoverageProblem():

	def __init__(self, grid_height=0, grid_width=0, wifi_range=0, goal_val=0, device_coords=(), initial_wifi_coords=()):
		State.grid_height = grid_height
		State.grid_width = grid_width
		State.wifi_range = wifi_range
		State.device_coords = device_coords

		self.grid_height = grid_height
		self.grid_width = grid_width
		self.wifi_range = wifi_range
		self.goal_val = goal_val
		self.device_coords = device_coords
		self.initial_state = State(wifi_coords=initial_wifi_coords)

	def check_constraints(self, state=State()):
		return (state.evaluate() >= self.goal_val)

	def show_solution(self, solution_state):
		grid = [[ ' ' for x in range(self.grid_width) ] for y in range(self.grid_height)]

		print(solution_state)
		for x, y in solution_state.wifi_coords:
			grid[x][y] = 'X'

		for x, y in self.device_coords:
			grid[x][y] = '*'

		for y in range(self.grid_height):
			print("|", end="")
			for x in range(self.grid_width):
				print(grid[x][y], end="")
			print("|")

		# plt.cla()
		# x, y = zip(*self.device_coords)
		# plt.plot(x, y, 'ro')
		# x, y = zip(*solution_state.wifi_coords)
		# plt.plot(x, y, 'b^')
		# plt.axis([0, 10, 0, 10])

		# ax = plt.gca()
		# for coord in solution_state.wifi_coords:
		# 	circle = plt.Circle(coord, self.wifi_range, color='g', fill=False)
		# 	ax.add_artist(circle)
		# 	ax.set_aspect('equal', 'box')

		# plt.show(block=False)
		# plt.pause(0.22)
		# plt.close()
	
	def show_final_sol(self, solution_state):
		plt.cla()
		x, y = zip(*self.device_coords)
		plt.plot(x, y, 'ro')
		x, y = zip(*solution_state.wifi_coords)
		plt.plot(x, y, 'b^')
		plt.axis([0, 10, 0, 10])

		ax = plt.gca()
		for coord in solution_state.wifi_coords:
			circle = plt.Circle(coord, self.wifi_range, color='g', fill=False)
			ax.add_artist(circle)
			ax.set_aspect('equal', 'box')

		plt.show()

	def get_initial_state(self):
		return self.initial_state

	def get_random_state(self):
		state = []
		for i in range(len(self.initial_state.wifi_coords)):
			state.append((
				random.randrange(0, self.grid_width),
				random.randrange(0, self.grid_height)
			))
		return State(tuple(state))
