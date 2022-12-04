from django.urls import path
from .views import CampoCreate, AtividadeCreate
from . import views
urlpatterns = [
    path('cadastrar_campo/', CampoCreate.as_view(), name= 'cadastrar-campo'),
    path('cadastrar_atividade/', AtividadeCreate.as_view(), name= 'cadastrar-atividade'),
    
]