from django.urls import path

from . import views

urlpatterns = [
    path('', views.gameboy, name='console'),
    path('moviedex', views.moviedex, name ='moviedex'),
    path('battle', views.battle, name='battletemplate'),
]