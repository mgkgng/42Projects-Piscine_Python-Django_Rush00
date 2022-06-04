from this import d
import random
from movie import request_omdb

class Game:
	def __init__(self):
		self.MovieMons = request_omdb() # a voir
		self.playerStrength = 1.0 # a voir
		self.position = (0, 0)
		self.movieballsNb = 0
		self.moviedex = []

class Player:
	def __init__(self):
		self.MovieMons = request_omdb()
		self.playerStrength = 1.0

	#### member functiosn asked in the subject ####

	def load(self, game):
		self.position = game.position
		self.movieballsNb = game.movieballsNb
		self.moviedex = game.moviedex

	def dump(self):
		save = Game()
		save.playerStrength = self.playerStrength
		save.position = self.position
		save.movieballsNb = self.movieballsNb
		save.moviedex = self.moviedex
		save.playerStrength = self.playerStrength
		return save

	def get_random_movie(self):
		random.choice(self.MovieMons)

	def load_default_settings(self):
		pass

	def get_strength(self):
		return self.playerStrength

	def get_movie(self, name):
		return self.MovieMons["name"]