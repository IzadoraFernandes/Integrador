from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path("__reload__/", include("django_browser_reload.urls")), 
    path('reservas_sala/<int:pk>', views.ReservaSalaListView.as_view(), name='reservas-sala'),
]
