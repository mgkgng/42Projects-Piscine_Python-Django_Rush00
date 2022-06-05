from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap
import random

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

