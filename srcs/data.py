from this import d
import random
from movie import request_omdb

class Game:
	def __init__(self, MovieMons, playerStrength, position, movieballsNb, moviedex):
		self.MovieMons = MovieMons
		self.playerStrength = playerStrength
		self.position = position
		self.movieballsNb = movieballsNb
		self.moviedex = moviedex

class Player:
	def __init__(self):
		self.load_default_settings()

	#### member functiosn asked in the subject ####

	def load(self, game):
		self.MovieMons = game.MovieMons
		self.playerStrength = game.playerStrength
		self.position = game.position
		self.movieballsNb = game.movieballsNb
		self.moviedex = game.moviedex

	def dump(self):
		save = Game(self.MovieMons, 
				self.playerStrength, 
				self.position, 
				self.movieballsNb, 
				self.moviedex)
		return save

	def get_random_movie(self):
		return random.choice(self.MovieMons).keys() # have to check later

	def load_default_settings(self):
		self.MovieMons = request_omdb()
		self.playerStrength = 3.0
		self.position = (0, 0)
		self.movieballsNb = 0
		self.moviedex = []

	def get_strength(self):
		return self.playerStrength

	def get_movie(self, name):
		return self.MovieMons["name"]