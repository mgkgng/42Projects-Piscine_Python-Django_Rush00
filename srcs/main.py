import re
import requests, json, sys

def request_omdb(moviename):
	S = requests.Session()
	URL = "http://www.omdbapi.com/?i=tt3896198&apikey=c4f868ed"

	R = S.get(url=URL)
	DATA = R.json()

	PARAMS = {
		"s": moviename,
		"r": "json",
	}

	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()

	print(json.dumps(DATA, sort_keys=True, indent=4))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit(0)
	request_omdb(sys.argv[1])