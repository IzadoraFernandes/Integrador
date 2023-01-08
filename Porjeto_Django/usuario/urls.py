from django.urls import path, include
from . import views


urlpatterns = [
    path ('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path ('register/login/', views.login, name='login'),
    path ('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path ('usuarios/', views.usuarios, name='usuarios'),
    path("register/", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]