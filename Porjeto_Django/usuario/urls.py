from django.urls import path
from . import views

urlpatterns = [
    path ('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path ('login/', views.login, name='login'),
    path ('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
]