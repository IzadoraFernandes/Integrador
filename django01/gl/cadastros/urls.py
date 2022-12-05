from django.urls import path
from .views import SalaCreate, ReservaCreate
from . import views
urlpatterns = [
    path('cadastrar_campo/', SalaCreate.as_view(), name= 'cadastrar_campo'),
    path('cadastrar_atividade/', ReservaCreate.as_view(), name= 'cadastrar_atividade'),
    
]