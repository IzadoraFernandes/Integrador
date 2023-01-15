from django.urls import path
#from . import views
from .views import Cadastrar_labView, Cadastrar_reservaView, Cadastrar_salaView, InformaticaView, ApiculturaView, AlimentosView, QuimicaView #, TesteView
urlpatterns = [
    
    path('cadastrar_lab/', Cadastrar_labView.as_view(), name = 'cadastrar_lab'),
    path('cadastrar_reserva/', Cadastrar_reservaView.as_view(), name = 'cadastrar_reserva'),
    path('cadastrar_sala/', Cadastrar_salaView.as_view(), name = 'cadastrar_sala'),
    path('informatica/', InformaticaView.as_view(), name = 'informatica'),
    path('alimentos/', AlimentosView.as_view(), name = 'alimentos'),
    path('apicultura/', ApiculturaView.as_view(), name = 'apicultura'),
    path('quimica/', QuimicaView.as_view(), name = 'quimica'),
    #path('teste/', TesteView.as_view(), name = 'teste'),
    #path ('cadastrar_lab/', views.cadastrar_lab, name='cadastrar_lab'),
    #path ('cadastrar_reserva/', views.cadastrar_reserva, name='cadastrar_reserva'),
    #path ('cadastrar_sala/', views.cadastrar_sala, name='cadastrar_sala'),
    #path ('informatica/', views.informatica, name='informatica'),
    #path ('alimentos/', views.alimentos, name='alimentos'),
    #path ('apicultura/', views.apicultura, name='apicultura'),
    #path ('quimica/', views.quimica, name='quimica'),

   
    
]
