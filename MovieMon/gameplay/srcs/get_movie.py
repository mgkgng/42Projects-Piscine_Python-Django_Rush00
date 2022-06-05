import requests, json, os

def request_omdb():
	res = dict()

	movielist = open(os.getcwd() + "/gameplay/srcs/movielist.txt", 'r').readlines()

	S = requests.Session()
	URL = "http://www.omdbapi.com/?i=tt3896198&apikey=c4f868ed"

	R = S.get(url=URL)
	DATA = R.json()

	for movie in movielist:
		moviename = movie.rstrip("\n")
		PARAMS = {
			"t": moviename,
			"type": "movie",
			"r": "json",
		}
		R = S.get(url=URL, params=PARAMS)
		if (R.status_code == 404):
			print("Error encountered while requesting to omdb api")
			exit(1)
		DATA = R.json()
		res[moviename] = DATA
	facile = json.dumps(res["The Ring"], sort_keys=True, indent=4)
	print(facile)
	return res