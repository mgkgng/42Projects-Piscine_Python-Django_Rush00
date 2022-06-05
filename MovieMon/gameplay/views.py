from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .srcs.worldmap import Worldmap
from .srcs.data import Player
from .srcs.data import Game
import random

global worldmap
global current_player
global index
global loaded
index = int(0)
loaded = int(0)
msg = ""
msg_battle = ""
battle = False
caught = False


def titlepage(request):
    global worldmap
    global current_player
    if request.GET.get('button') == "A":
        current_player = Player()
        worldmap = Worldmap()
        return redirect('/gameplay', {"path": "gameplay"})
    elif request.GET.get('button') == "B":
        if worldmap == None:
            worldmap = Worldmap()
        return (redirect("/options/load_game", {"path": "/options/load_game"}))
    return render(request, "html/titlepage.html", {"path": ""})

def load(request) :
    global index
    global loaded
    global worldmap
    global current_player
    l = len(current_player.game.moviedex)
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
                current_game = current_player.game.load("third")
                loaded = 1
                return redirect('/gameplay', {"path": "gameplay"})
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

def make_event(request):
    global msg
    global current_game

    event = [None, "Movieball", "MovieMon"]
    elem = random.choices(event, weights=(60, 30, 10), k=1)
    if elem[0] == "Movieball":
        msg = "You found a Movieball!"
        current_player.game.movieballsNb += 1
        return redirect('/gameplay', {"path": "gameplay", "msg": msg , "movieballNb" : str(current_player.game.movieballsNb) + msg, 
            "index_x": str(current_player.game.position[0]), "index_y": str(current_player.game.position[1])})
    elif elem[0] == "MovieMon":
        global battle
        global caught
        msg = "MovieMon flushed out! (Press A to continue)"
        battle = True
        caught = False
        #return redirect("/battle/" + movie_id, {"path": f"battle/{movie_id}"})
        return redirect("/gameplay", {"battle": True, "path": "battle", "msg": msg, "movieballNb" : str(current_player.game.movieballsNb), 
            "index_x": str(current_player.game.position[0]), "index_y": str(current_player.game.position[1])})
    else:
        msg = ""
        return redirect('/gameplay', {"path": "gameplay", "movieballNb" : str(current_player.game.movieballsNb), 
            "index_x": str(current_player.game.position[0]), "index_y": str(current_player.game.position[1])})

def gameplay(request):
    global msg
    global battle
    global caught
    global current_Game
    #if 'worldmap' not in globals():
    #    redirect('/titlepage')
    if battle == True:
        if request.GET.get('button') == "A":
            movie_id = current_player.get_random_movie()["imdbID"]
            msg=""
            return HttpResponseRedirect(reverse("battle", args=(movie_id, )))
        else:
            return render(request, "html/worldmap.html", {"path": "gameplay", "msg": msg, "movieballNb" : str(current_player.game.movieballsNb), 
            "index_x": str(current_player.game.position[0]), "index_y": str(current_player.game.position[1])})
 
    if request.GET.get('button') == "START":
        return redirect('/options', {"path": "options"})
    if request.GET.get('button') == "SELECT":
        return redirect('/moviedex', {"path": "moviedex"})
    if request.GET.get('button') == "UP":
        if current_player.game.position[0] > 0:
            current_player.game.position[0] -= 1
            return make_event(request)
    elif request.GET.get('button') == "DOWN":
        if current_player.game.position[0] < 9:
            current_player.game.position[0] += 1
            return make_event(request)
    elif request.GET.get('button') == "LEFT":
        if current_player.game.position[1] > 0:
            current_player.game.position[1] -= 1
            return make_event(request)
    elif request.GET.get('button') == "RIGHT":
        if current_player.game.position[1] < 9:
            current_player.game.position[1] += 1
            return make_event(request)
    return render(request, "html/worldmap.html", {"path": "gameplay", "msg": msg, "movieballNb" : str(current_player.game.movieballsNb), 
        "index_x": str(current_player.game.position[0]), "index_y": str(current_player.game.position[1])})

def moviedex(request) :
    global index
    global current_game

    imgdex = [current_player.game.MovieMons[moviename]["Poster"] for moviename in current_player.game.MovieMons.keys()]
    if request.GET.get('button') == "SELECT":
        return redirect('/gameplay', {"path": "gameplay"})

    if request.GET.get('button') == "LEFT":
        if index > 0:
            index -= 1
    elif request.GET.get('button') == "RIGHT":
        if index < len(imgdex) - 1:
            index += 1
    print(str(index) + "   this is value " + str(len(imgdex)))
    choice = imgdex[index]
    #mydict = {}#Remplir des images des moviemons attrapes
    return render (request,"html/moviedex.html", {"path": "moviedex", "img" : imgdex, "choice" : choice})

def battle(request, monster_id) :
    global msg
    global worldmap
    global battle
    global caught
    global current_player

    battle = False
    msg_battle = ""
    if current_player.game.movieballsNb == 0 and caught == False:
        msg_battle = "No more movieball left!"
    movie = current_player.get_movie_by_id(monster_id)
    result = 0
    if caught == True:
        result = 1
    c = 50 - (float(movie["imdbRating"]) * 10) + (current_player.get_strength() * 5)
    if c < 1:
        c = 1
    elif c > 90:
        c = 90
    if request.GET.get('button') == "A" and caught == False:
        if current_player.game.movieballsNb == 0:
            return HttpResponseRedirect(reverse("battle", args=(monster_id, )))
        else:
            current_player.game.movieballsNb -= 1
            catch = random.choices([1, 2], weights=(c, 100 - c), k=1)
            result = catch[0]
            if result == 1:
                current_player.game.moviedex.append(movie)
                caught = True
    elif request.GET.get('button') == "B":
        return redirect("/gameplay", {"path": "gameplay"})
    mydict = {}
    mydict["msg"] = msg_battle
    mydict["movieballs"] = current_player.game.movieballsNb
    mydict["strength"] = current_player.game.playerStrength
    mydict["winrate"] = c
    mydict["success"] = result
    mydict["image"] = movie["Poster"]        
    return render(request, "html/battle.html", mydict)

def options(request) :
    if request.GET.get('button') == "A":
        return redirect('/options/save_game', {"path": "/options/save_game"})
    if request.GET.get('button') == "START":
        return redirect('/gameplay', {"path": "gameplay"})
    if request.GET.get('button') == "B":
        return redirect('/', {"path": "/"})
    return render(request, "html/options.html")

def save(request) :
    global index
    global worldmap
    global current_player

    l1, l2, l3 = "None", "None", "None"
    if worldmap.Games[0] != None:
        l1 = str(len(worldmap.Games[0].game.moviedex)) + " / 15"
    if worldmap.Games[1] != None:
        l2 = str(len(worldmap.Games[1].game.moviedex)) + " / 15"
    if worldmap.Games[2] != None:
        l3 = str(len(worldmap.Games[2].game.moviedex)) + " / 15"
    if request.GET.get('button') == "B":
        return redirect('/options', {"path": "options"})
    if request.GET.get('button') == "UP":
        if index > 0:
            index -= 1
    elif request.GET.get('button') == "DOWN":
        if index < 2:
            index += 1
    elif request.GET.get('button') == "A":
        current_player.dump(str(index))

    return render(request, "html/save.html", {"A" : l1, "B": l2, "C": l3, "index" : index})


