from django.urls import path

from . import views

urlpatterns = [
    path('', views.gameboy, name='console'),
]