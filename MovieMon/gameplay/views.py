from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap
from .srcs.data import Player
import random

global worldmap 

#worldmap.Player.MovieMons["moviename"]["Poster"]

def moviedex(request) :
    worldmap = Worldmap(10, 10)
    list = [worldmap.Player.MovieMons[moviename]["Poster"] for moviename in worldmap.Player.MovieMons.keys()]
    print(list)
    i = 0
    #mydict = {}#Remplir des images des moviemons attrapes
    return render (request,"html/moviedex.html", {"img" : list, "index" : i})

def battle(request) :
    movieballs = 10
    strength = 97
    winrate = 20
    mydict = {}
    mydict["movieballs"] = 10
    mydict["strength"] = 97
    mydict["winrate"] = 20
    mydict["success"] = random.randint(0, 1)
    return render(request, "html/battle.html", mydict)

def gameboy(request):
    return render(request, "html/gameboy.html")

