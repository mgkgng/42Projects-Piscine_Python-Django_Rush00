import re
import requests, json, sys

def request_omdb(moviename):
	S = requests.Session()
	URL = "http://www.omdbapi.com/?i=tt3896198&apikey=c4f868ed"

	R = S.get(url=URL)
	DATA = R.json()

	PARAMS = {
		"t": moviename,
		"type": "movie",
		"r": "json",
	}

	R = S.get(url=URL, params=PARAMS)
	if (R.status_code == 404):
		print("Movie not found.")
		exit(1)
	DATA = R.json()
	return DATA["imdbRating"]


if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit(0)
	request_omdb(sys.argv[1])