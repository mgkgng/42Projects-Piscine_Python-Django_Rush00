from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap
import random

global worldmap
global now

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

def moviedex(request) :
    print(request.GET.get("value"))
    now = 2
    worldmap = Worldmap(10, 10)
    imgdex = [worldmap.Player.MovieMons[moviename]["Poster"] for moviename in worldmap.Player.MovieMons.keys()]
    if request.GET.get('button') == "LEFT":
        print("hello")
        if now > 0:
            now -= 1
    elif request.GET.get('button') == "RIGHT":
        if now < len(imgdex):
            now += 1
    choice = imgdex[now]
    #mydict = {}#Remplir des images des moviemons attrapes
    return render (request,"html/moviedex.html", {"path": "moviedex", "img" : imgdex, "choice" : choice})

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
