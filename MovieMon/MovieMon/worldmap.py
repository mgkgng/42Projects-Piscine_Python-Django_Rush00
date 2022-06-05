from .data import Game, Player

class Worldmap:
	def __init__(self, grid_x, grid_y):
		self.mapSize = (grid_x, grid_y)
		self.Player = Player()
