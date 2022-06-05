from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap
from .srcs.data import Player
import random

worldmap = Worldmap(10, 10)

#worldmap.Player.MovieMons["moviename"]["Poster"]

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

def input(request):
    pass

def worldmap(request):
    pass

def buttonUp(request):
    pass

def buttonDown(request):
    pass

def buttonMiddleLeft(request):
    pass

def buttonMiddleRight(request):
    pass

def buttonA(request):
    pass

def buttonB(request):
    pass

def buttonStart(request):
    pass

def buttonSelect(request):
    pass
