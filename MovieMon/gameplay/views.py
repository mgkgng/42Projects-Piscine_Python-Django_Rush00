from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap

worldmap = Worldmap(10, 10)

def titlepage(request):
    if request.GET.get('button') == "A":
        return (render(request, "html/worldmap.html", {"path": "gameplay"}))
    elif request.GET.get('button') == "B":
        return (render(request, "html/titlepage.html"), {})
    return render(request, "html/titlepage.html", {"path": ""})

def load(request):
    if request.GET.get('button') == "A":
        pass
    if request.GET.get('button') == "B":
        pass
    return render(request, "html/load.html")

def gameplay(request, game):
    print(request.GET.get('button'))
    #form = Button()
    return render(request, "html/worldmap.html", {"path": "gameplay"})