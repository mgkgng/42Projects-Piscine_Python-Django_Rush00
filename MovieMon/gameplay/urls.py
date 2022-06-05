from django.urls import path

from . import views

urlpatterns = [
    path('', views.titlepage, name='titlepage'),
    path('gameplay', views.gameplay, name='gameplay'),
    path('battle/<monster_id>', views.battle, name='battle'),
    path('battle', views.battle, name='battletemplate'),
    path('moviedex', views.moviedex, name ='moviedex'),
    path('options', views.options, name ='options'),
    path('options/save_game', views.save, name ='save'),
    path('options/load_game', views.load, name ='load'),
    path('load', views.load, name ='load'),
    path('save', views.save, name ='save') 
]