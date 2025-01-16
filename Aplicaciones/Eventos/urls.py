from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('listadoAdministradores/', views.listadoAdministradores, name='listadoAdministradores'),
    path('crearAdministrador/', views.crearAdministrador, name='crearAdministrador'),
    path('listadoClientes/', views.listadoClientes, name='listadoClientes'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
]
