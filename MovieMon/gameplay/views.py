from django.shortcuts import render, HttpResponse
from .srcs.worldmap import Worldmap

worldmap = Worldmap(10, 10)

def gameboy(request):
    return render(request, "html/gameboy.html")

def input(request):
    pass

def worldmap(request):
    pass

def buttonUp(request):
    pass

def buttonDown(request):
    pass

def buttonMiddleLeft(request):
    pass

def buttonMiddleRight(request):
    pass

def buttonA(request):
    pass

def buttonB(request):
    pass

def buttonStart(request):
    pass

def buttonSelect(request):
    pass
