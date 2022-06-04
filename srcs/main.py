import re
import requests, json, sys

def request_omdb():
	res = dict()

	movielist = open("movielist.txt", 'r').readlines()
	request_omdb(movielist)

	S = requests.Session()
	URL = "http://www.omdbapi.com/?i=tt3896198&apikey=c4f868ed"

	R = S.get(url=URL)
	DATA = R.json()

	for movie in movielist:
		PARAMS = {
			"t": movie,
			"type": "movie",
			"r": "json",
		}

		R = S.get(url=URL, params=PARAMS)
		if (R.status_code == 404):
			print("Error encountered while requesting to omdb api")
			exit(1)
		DATA = R.json()
		res[movie] = DATA["imdbRating"]

	return res

if __name__ == "__main__":
	request_omdb()