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
    path('listadoOrganizadorID/<id>/', views.listadoOrganizadorID, name='listadoOrganizadorID'),
    path('actualizar_organizador/', views.actualizar_organizador, name='actualizar_organizador'),
    path('eliminarUsuario/<id>', views.eliminarUsuario, name='eliminarUsuario'),
    
    path('festival_list/', views.festival_list, name='festival_list'),
    path('crear_festival/', views.crear_festival, name='crear_festival'),
    path('listadoFestivalID/<id>/', views.listadoFestivalID, name='listadoFestivalID'),  
    path('actualizar_festival/', views.actualizar_festival, name='actualizar_festival'),  
    path('deleteFestival/<id>/', views.deleteFestival, name='deleteFestival'),  
    
    path('listLicences/', views.listLicences, name='listLicences'),
    path('createLicence/', views.createLicence, name='createLicence'),
    path('listLicencesID/<id>/', views.listLicencesID, name='listLicencesID'),
    path('updateLicence/', views.updateLicence, name='updateLicence'),
    path('deleteLicence/<id>/', views.deleteLicence, name='deleteLicence'),
    
    path('listAudits/', views.listAudits, name='listAudits'),
    path('createAudit/', views.createAudit, name='createAudit'),
    path('listAuditsID/<id>/', views.listAuditsID, name='listAuditsID'),
    path('updateAudit/', views.updateAudit, name='updateAudit'),
    path('deleteAudit/<id>/', views.deleteAudit, name='deleteAudit'),
    
    
    
]
