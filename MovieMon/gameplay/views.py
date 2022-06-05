from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap
import random

<<<<<<< HEAD
global worldmap 

#worldmap.Player.MovieMons["moviename"]["Poster"]
=======
global worldmap

def titlepage(request):
    if request.GET.get('button') == "A":
        worldmap = Worldmap(20, 20)
        return (render(request, "html/worldmap.html", {"path": "gameplay"}))
    elif request.GET.get('button') == "B":
        return (render(request, "html/load.html"), {})
    return render(request, "html/titlepage.html", {"path": ""})

def load(request):
    if request.GET.get('button') == "A":
        pass
    if request.GET.get('button') == "B":
        pass
    return render(request, "html/load.html")

def gameplay(request, game):
    if request.GET.get('button') == "UP":
        if worldmap.Player.position[1] > 0:
            worldmap.Player.position[1] -= 1
    elif request.GET.get('button') == "DOWN":
        if worldmap.Player.position[1] < worldmap.mapSize[1]:
            worldmap.Player.position[1] += 1
    elif request.GET.get('button') == "LEFT":
        if worldmap.Player.position[0] > 0:
            worldmap.Player.position[0] -= 1
    elif request.GET.get('button') == "RIGHT":
        if worldmap.Player.position[1] < worldmap.mapSize[0]:
            worldmap.Player.position[1] += 1

    print(request.GET.get('button')) 
    #form = Button()
    return render(request, "html/worldmap.html", {"path": "gameplay"})
>>>>>>> feature/battle

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
<<<<<<< HEAD
    return render(request, "html/battle.html", mydict)

def gameboy(request):
    return render(request, "html/gameboy.html")

=======
    return render(request, "html/battle.html", mydict)
>>>>>>> feature/battle
