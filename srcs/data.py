from this import d
import random
from movie import request_omdb

class Data:
	def __init__(self):
		self.MovieMons = request_omdb()
		self.playerStrength = 1.0

	def load(self):
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