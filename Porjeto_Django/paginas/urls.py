from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu_salas/', views.menu_salas, name='menu_salas'),
    path('agenda/', views.agenda, name='agenda'),
    path("__reload__/", include("django_browser_reload.urls")),    
]
