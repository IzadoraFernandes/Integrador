from django.urls import path
#from . import views
from .views import  CadastrarReservaView, ReservaListView, ReservaUpdateView,ReservaDeleteView, CadastrarSalaView, SalasListView, SalasUpdateView, SalasDeleteView

urlpatterns = [
    
    #path('cadastrar_lab/', Cadastrar_labView.as_view(), name = 'cadastrar_lab'),
    path('cadastrar_reserva/', CadastrarReservaView.as_view(), name = 'cadastrar_reserva'),
    path('teste/', ReservaListView.as_view(), name = 'teste'),
    path('<int:pk>/update-reserva/', ReservaUpdateView.as_view(), name='update-reserva'),
    path('<int:pk>/delete-reserva/', ReservaDeleteView.as_view(), name='delete-reserva'),
    path('cadastrar_sala/', CadastrarSalaView.as_view(), name = 'cadastrar_sala'),
    path('salas/', SalasListView.as_view(), name = 'salas'),
    path('<int:pk>/update-salas/', SalasUpdateView.as_view(), name='update-salas'),
    path('<int:pk>/delete-salas/', SalasDeleteView.as_view(), name='delete-salas'), 
]
