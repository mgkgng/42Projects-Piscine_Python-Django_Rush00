from django.urls import path

from . import views

urlpatterns = [
    path('', views.titlepage, name='titlepage'),
    path('gameplay', views.gameplay, name='gameplay'),
    path('battle', views.battle, name='battle'),
]