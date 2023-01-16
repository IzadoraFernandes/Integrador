from django.urls import path
#from . import views
from .views import  CadastrarReservaView, Cadastrar_salaView, InformaticaView, ApiculturaView, AlimentosView, QuimicaView #, TesteView
urlpatterns = [
    
    #path('cadastrar_lab/', Cadastrar_labView.as_view(), name = 'cadastrar_lab'),
    path('cadastrar_reserva/', CadastrarReservaView.as_view(), name = 'cadastrar_reserva'),
    path('cadastrar_sala/', Cadastrar_salaView.as_view(), name = 'cadastrar_sala'),
    path('informatica/', InformaticaView.as_view(), name = 'informatica'),
    path('alimentos/', AlimentosView.as_view(), name = 'alimentos'),
    path('apicultura/', ApiculturaView.as_view(), name = 'apicultura'),
    path('quimica/', QuimicaView.as_view(), name = 'quimica'),

    
]
