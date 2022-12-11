from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu_salas/', views.menu_salas, name='menu_salas'),
    path('agenda/', views.agenda, name='agenda'),
    
]
