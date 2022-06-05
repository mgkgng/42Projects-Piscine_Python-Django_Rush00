from this import d


class MapData:
	def __init__(self, size):
		self.size = size

class Worldmap:
	def __init__(self, MapData, Player):
		self.MapData = MapData
		self.Player = Player

	def getScreen(self, grid_x, grid_y):
		start_x = self.Player.position[0] -  grid_x / 2
		if start_x < 0:
			start_x = 0
		elif start_x + grid_x / 2 > self.MapData.size:
			start_x = self.MapData.size - grid_x / 2
		start_y = self.Player.position[1] -  grid_y / 2
		if start_y < 0:
			start_y = 0
		elif start_y + grid_y / 2 > self.MapData.size:
			start_y = self.MapData.size - grid_y / 2
		
		for i in range(grid_x):
			
