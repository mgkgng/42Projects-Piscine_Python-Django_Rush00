from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .srcs.worldmap import Worldmap
import random

msg = ""
msg_battle = ""
battle = False
caught = False

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
        global caught
        msg = "MovieMon flushed out! (Press A to continue)"
        battle = True
        caught = False
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
    global caught
    #if 'worldmap' not in globals():
    #    redirect('/titlepage')
    if battle == True:
        if request.GET.get('button') == "A":
            movie_id = worldmap.Player.get_random_movie()["imdbID"]
            return HttpResponseRedirect(reverse("battle", args=(movie_id, )))
        else:
            return render(request, "html/worldmap.html", {"path": "gameplay", "msg": msg, "movieballNb" : str(worldmap.Player.movieballsNb), 
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

def battle(request, monster_id) :
    global msg
    global worldmap
    global battle

    battle = False
    msg_battle = ""
    if worldmap.Player.movieballsNb == 0:
        msg_battle = "No more movieball left!"
    movie = worldmap.Player.get_movie_by_id(monster_id)
    result = 0
    c = 50 - (float(movie["imdbRating"]) * 10) + (worldmap.Player.get_strength() * 5)
    if c < 1:
        c = 1
    elif c > 90:
        c = 90
    if request.GET.get('button') == "A" and caught == False:
        if worldmap.Player.movieballsNb == 0:
            return HttpResponseRedirect(reverse("battle", args=(monster_id, )))
        else:
            worldmap.Player.movieballsNb -= 1
            catch = random.choices([1, 2], weights=(c, 100 - c), k=1)
            result = catch[0]
            if result == 1:
                worldmap.Player.moviedex.append(movie)
    elif request.GET.get('button') == "B":
        return redirect("/gameplay", {"path": "gameplay"})

    mydict = {}
    mydict["msg"] = msg_battle
    mydict["movieballs"] = worldmap.Player.movieballsNb
    mydict["strength"] = worldmap.Player.playerStrength
    mydict["winrate"] = c
    mydict["success"] = result
    mydict["image"] = movie["Poster"]
    if result == 1:
        caught = True
    return render(request, "html/battle.html", mydict)