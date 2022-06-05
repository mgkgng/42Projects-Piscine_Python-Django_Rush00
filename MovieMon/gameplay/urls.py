from django.urls import path

from . import views

urlpatterns = [
    path('', views.gameboy, name='console'),
    path('battle', views.battle, name='battletemplate'),
    path('buttonUp', views.buttonUp, name='buttonUp'),
	path('buttonDown', views.buttonDown, name='buttonDown'),
	path('buttonMiddleLeft', views.buttonMiddleLeft, name='buttonMiddleLeft'),
    path('buttonMiddleRight', views.buttonMiddleRight, name='buttonMiddleRight'),
    path('buttonA', views.buttonA, name='buttonA'),
	path('buttonB', views.buttonB, name='buttonB'),
    path('buttonStart', views.buttonStart, name='buttonStart'),
	path('buttonSelect', views.buttonSelect, name='buttonSelect'),
]