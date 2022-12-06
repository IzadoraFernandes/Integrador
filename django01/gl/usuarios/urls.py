from django.urls import path
from .views import LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', LoginView.as_view(), name= 'login'),
    
]
