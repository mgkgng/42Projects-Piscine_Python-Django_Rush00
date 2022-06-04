from this import d
import random
from movie import request_omdb

class Game:
	def __init__(self):
		self.position = (0, 0)
		self.movieballsNb = 0
		self.moviedex = []
		

class Data:
	def __init__(self):
		self.MovieMons = request_omdb()
		self.playerStrength = 1.0

	def load(self, game):
		pass

	def dump(self):
		pass

	def get_random_movie(self):
		random.choice(self.MovieMons)

	def load_default_settings(self):
		pass

	def get_strength(self):
		return self.playerStrength

	def get_movie(self, name):
		return self.MovieMons["name"]