from django.shortcuts import render, HttpResponse, redirect
from .srcs.worldmap import Worldmap
import random

global worldmap
global index 
global loaded
index = int(0)
loaded = int(0)
msg = ""
battle = False


def titlepage(request):
    global worldmap
    if request.GET.get('button') == "A":
        worldmap = Worldmap(10, 10)
        return redirect('/gameplay', {"path": "gameplay"})
    elif request.GET.get('button') == "B":
        return (redirect("/load", {"path": "load"}))
    return render(request, "html/titlepage.html", {"path": ""})

def load(request):
    if request.GET.get('button') == "A":
        pass
    if request.GET.get('button') == "B":
        pass
    return render(request, "html/load.html")

def make_event(request):
    global msg
    event = [None, "Movieball", "MovieMon"]
    elem = random.choices(event, weights=(60, 30, 10), k=1)
    if elem[0] == "Movieball":
        msg = "You found a Movieball!"
        worldmap.Player.movieballsNb += 1
        return redirect('/gameplay', {"path": "gameplay", "msg": msg , "movieballNb" : str(worldmap.Player.movieballsNb) + msg, 
            "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})
    elif elem[0] == "MovieMon":
        global battle
        msg = "MovieMon flushed out! (Press A to continue)"
        battle = True
        #return redirect("/battle/" + movie_id, {"path": f"battle/{movie_id}"})
        return redirect("/gameplay", {"battle": True, "path": "battle", "msg": msg, "movieballNb" : str(worldmap.Player.movieballsNb), 
            "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})
    else:
        msg = ""
        return redirect('/gameplay', {"path": "gameplay", "movieballNb" : str(worldmap.Player.movieballsNb), 
            "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})

def gameplay(request):
    global msg
    global battle
    #if 'worldmap' not in globals():
    #    redirect('/titlepage')
    if battle == True:
        if request.GET.get('button') == "A":
            movie_id = worldmap.Player.get_random_movie()["imdbID"]
            return redirect("/battle/" + movie_id, {"path": f"battle/{movie_id}"})
        else:
            return render(request, "html/worldmap.html", {"path": "battle", "msg": msg, "movieballNb" : str(worldmap.Player.movieballsNb), 
            "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})
 
    if request.GET.get('button') == "UP":
        if worldmap.Player.position[0] > 0:
            worldmap.Player.position[0] -= 1
            return make_event(request)
    elif request.GET.get('button') == "DOWN":
        if worldmap.Player.position[0] < 9:
            worldmap.Player.position[0] += 1
            return make_event(request)
    elif request.GET.get('button') == "LEFT":
        if worldmap.Player.position[1] > 0:
            worldmap.Player.position[1] -= 1
            return make_event(request)
    elif request.GET.get('button') == "RIGHT":
        if worldmap.Player.position[1] < 9:
            worldmap.Player.position[1] += 1
            return make_event(request)
    return render(request, "html/worldmap.html", {"path": "gameplay", "msg": msg, "movieballNb" : str(worldmap.Player.movieballsNb), 
        "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})

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
    mydict["movieballs"] = worldmap.Player.movieballNb
    mydict["strength"] = worldmap.Player.playerStrength
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
