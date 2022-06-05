import random, pickle
from get_movie import request_omdb

class Game:
	def __init__(self, MovieMons, playerStrength, position, movieballsNb, moviedex):
		self.MovieMons = MovieMons
		self.playerStrength = playerStrength
		self.position = position
		self.movieballsNb = movieballsNb
		self.moviedex = moviedex

class Player:
	def __init__(self, save = None):
		if save == None:
			self.load_default_settings()
		else:
			self.load(save)

	#### member functiosn asked in the subject ####
	def load(self, saveName):
		with open(saveName, "rb") as f:
			loadGame = pickle.load(f)
		self.MovieMons = loadGame.MovieMons
		self.playerStrength = loadGame.playerStrength
		self.position = loadGame.position
		self.movieballsNb = loadGame.movieballsNb
		self.moviedex = loadGame.moviedex

	def dump(self, saveName):
		save = Game(self.MovieMons, 
				self.playerStrength, 
				self.position, 
				self.movieballsNb, 
				self.moviedex)
		with open(saveName, "wb") as f:
			pickle.dump(save, f)

	def get_random_movie(self):
		return random.choice(self.MovieMons).keys() # have to check later

	def load_default_settings(self):
		self.MovieMons = request_omdb()
		self.playerStrength = 3.0
		self.position = (8, 8)
		self.movieballsNb = 0
		self.moviedex = []

	def get_strength(self):
		return self.playerStrength

	def get_movie(self, name):
		return self.MovieMons["name"]