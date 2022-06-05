from django.shortcuts import render, HttpResponse, redirect
from .srcs.worldmap import Worldmap
import random

global worldmap
global index 
global loaded
index = int(0)
loaded = int(0)

def titlepage(request):
    if request.GET.get('button') == "A":
        worldmap = Worldmap(20, 20)
        index = 0
        return (render(request, "html/worldmap.html", {"path": "gameplay"}))
    elif request.GET.get('button') == "B":
        return (render(request, "html/load.html"), {})
    return render(request, "html/titlepage.html", {"path": ""})

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

    #form = Button()
    return render(request, "html/worldmap.html", {"path": "gameplay"})

def moviedex(request) :
    global index
    worldmap = Worldmap(10, 10)
    imgdex = [worldmap.Player.MovieMons[moviename]["Poster"] for moviename in worldmap.Player.MovieMons.keys()]
    if request.GET.get('button') == "LEFT":
        if index > 0:
            index -= 1
    elif request.GET.get('button') == "RIGHT":
        if index < len(imgdex):
            index += 1
    print(str(index) + "   this is value " + str(len(imgdex)))
    choice = imgdex[index]
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

def detail(request) :
    mydict = {}
    mydict["name"] = "Pulp Fiction"
    mydict["director"] = "Tarantino"
    mydict["year"] = "1994"
    mydict["rating"] = "10"
    mydict["synopsis"] = "Drogues, armes, mafia"
    mydict["actors"] = "tarantino, travolta"
    mydict["Bback"] = "test"
    return render(request, "html/detail.html", mydict)

def options(request) :
    return render(request, "html/options.html")

def save(request) :
    global index
    worldmap = Worldmap(10, 10)
    l = len(worldmap.Player.moviedex)
    if request.GET.get('button') == "UP":
        if index > 0:
            index -= 1
    elif request.GET.get('button') == "DOWN":
        if index < 2:
            index += 1
    return render(request, "html/save.html", {"A" : l, "index" : index})

def load(request) :
    global index
    global loaded
    worldmap = Worldmap(10, 10)
    l = len(worldmap.Player.moviedex)
    l1 = 0
    l2 = 0
    if request.GET.get('button') == "UP":
        if index > 0:
            index -= 1
    elif request.GET.get('button') == "DOWN":
        if index < 2:
            index += 1
    elif request.GET.get('button') == "A":
        if loaded == 0:
            if l != 0 and index == 0:
                #load save 0
                loaded = 1
            if l1 != 0 and index == 1:
                #load save1
                loaded = 1
            if l2 != 0 and index == 2:
                #load save2
                loaded = 1
        elif loaded == 1:
            loaded = 0
            #Go to worldmap
    return render(request, "html/load.html", {"A" : l, "B" : l1, "C" : l2, "index" : index, "loaded" : loaded})
