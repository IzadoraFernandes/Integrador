from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('menu_sala/', views.menu_sala, name='menu_sala'),
]