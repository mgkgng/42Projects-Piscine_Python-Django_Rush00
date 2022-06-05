from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.gameboy, name='console'),
    path('moviedex', views.moviedex, name ='moviedex'),
=======
    path('', views.titlepage, name='titlepage'),
    path('gameplay', views.gameplay, name='gameplay'),
>>>>>>> feature/battle
    path('battle', views.battle, name='battletemplate'),
]