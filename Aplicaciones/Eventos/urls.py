from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('listadoAdministradores/', views.listadoAdministradores, name='listadoAdministradores'),
    path('crearAdministrador/', views.crearAdministrador, name='crearAdministrador'),
    path('listadoAdministradorID/<id>/', views.listadoAdministradorID, name='listadoAdministradorID'),  
    path('actualizar_administrador/', views.actualizar_administrador, name='actualizar_administrador'),  
    path('listadoClientes/', views.listadoClientes, name='listadoClientes'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('listadoArtista/', views.listadoArtista, name='listadoArtista'),
    path('crearArtista/', views.crearArtista, name='crearArtista'),
    path('listadoArtistaID/<id>/', views.listadoArtistaID, name='listadoArtistaID'),  
    path('actualizar_artista/', views.actualizar_artista, name='actualizar_artista'),  
    path('listadoOrganizadores/', views.listadoOrganizadores, name='listadoOrganizadores'),
    path('crearOrganizadores/', views.crearOrganizadores, name='crearOrganizadores'),
    path('festival_list/', views.festival_list, name='festival_list'),
    path('crear_festival/', views.crear_festival, name='crear_festival'),
    
]
