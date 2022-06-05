from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap

worldmap = Worldmap(10, 10)

def titlepage(request):
    return render(request, "html/titlepage.html", {"path": titlepage})

def gameboy(request):
    print(request.GET.get('value'))
    #form = Button()
    return render(request, "html/gameboy.html")