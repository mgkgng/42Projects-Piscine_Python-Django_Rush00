from django.shortcuts import render, HttpResponse

def gameboy(request):
    return render(request, "html/titlescreen.html")