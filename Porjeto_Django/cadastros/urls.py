from django.urls import path
from . import views

urlpatterns = [
    path ('cadastrar_lab/', views.cadastrar_lab, name='cadastrar_lab'),
    path ('cadastrar_reserva/', views.cadastrar_reserva, name='cadastrar_reserva'),
    path ('cadastrar_sala/', views.cadastrar_sala, name='cadastrar_sala'),
    path ('informatica/', views.informatica, name='informatica'),
    path ('alimentos/', views.alimentos, name='alimentos'),
    path ('apicultura/', views.apicultura, name='apicultura'),
    path ('quimica/', views.quimica, name='quimica'),
    
]
