import random, pickle
from .get_movie import request_omdb

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
		self.game = Game(loadGame.MovieMons, loadGame.playerStrength, loadGame.position, 
			loadGame.movieballsNb, loadGame.moviedex)

	def dump(self, saveName):
		with open(saveName, "wb") as f:
			pickle.dump(self.game, f)

	def get_random_movie(self):
		keys = list(self.game.MovieMons)
		choice = random.choice(keys)
		return self.game.MovieMons[str(choice)] # have to check later

	def load_default_settings(self):
		self.game = Game(request_omdb(), 10, [5, 5], 0, [])

	def get_strength(self):
		return self.game.playerStrength

	def get_movie(self, name):
		return self.game.MovieMons["name"]

	def get_movie_by_id(self, movie_id):
		for moviename in self.game.MovieMons.keys():
			if self.game.MovieMons[moviename]["imdbID"] == movie_id:
				return self.game.MovieMons[moviename]
