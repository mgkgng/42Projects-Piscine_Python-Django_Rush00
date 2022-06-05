from django.shortcuts import render, redirect
from .srcs.worldmap import Worldmap
import random

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

def gameplay(request):
    #if 'worldmap' not in globals():
    #    redirect('/titlepage')
    if request.GET.get('button') == "UP":
        if worldmap.Player.position[0] > 0:
            worldmap.Player.position[0] -= 1
    elif request.GET.get('button') == "DOWN":
        if worldmap.Player.position[0] < 9:
            worldmap.Player.position[0] += 1
    elif request.GET.get('button') == "LEFT":
        if worldmap.Player.position[1] > 0:
            worldmap.Player.position[1] -= 1
    elif request.GET.get('button') == "RIGHT":
        if worldmap.Player.position[1] < 9:
            worldmap.Player.position[1] += 1

    msg = ""
    movieballNb = worldmap.Player.movieballsNb

    event = [None, "Movieball", "MovieMon"]
    elem = random.choices(event, weights=(85, 10, 5))
    if elem == "Movieball":
        msg = "You found a Movieball!"
        movieballNb += 1
    elif elem == "MovieMon":
        msg = "MovieMon flushed out! (Press A to continue)"
        movie_id = worldmap.Player.get_random_movie()["Poster"]
        redirect("/battle/" + movie_id, {"path": f"battle/{movie_id}"})
        return render(request, "html/battle.html")
 
    return render(request, "html/worldmap.html", {"path": "gameplay", "msg": msg, "movieballNb" : movieballNb, 
        "index_x": str(worldmap.Player.position[0]), "index_y": str(worldmap.Player.position[1])})

def battle(request, id) :
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