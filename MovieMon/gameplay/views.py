from django.shortcuts import render, redirect
from .srcs.worldmap import Worldmap
import random

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

def battle(request, slug) :
    if request.GET.get('button') == "A":
        pass
    elif request.GET.get('button') == "B":
        pass

    strength = 97
    winrate = 20
    mydict = {}
    mydict["movieballs"] = worldmap.Player.movieballNb
    mydict["strength"] = worldmap.Player.playerStrength
    mydict["winrate"] = 20
    mydict["success"] = random.randint(0, 1)
    return render(request, "html/battle.html", mydict)