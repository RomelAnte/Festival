from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Festival, Usuario, TipoUsuario, Biografía
import random

# Create your views here.

def index(request):
    return render(request, 'Pages/home.html')

def login(request):
    return render(request, 'Pages/login.html')

def inicio(request):
    admin = Usuario.objects.filter(tipo_usuario = 1).count()
    artistas = Usuario.objects.filter(tipo_usuario = 2).count()
    organizadores = Usuario.objects.filter(tipo_usuario = 3).count()
    asistentes = Usuario.objects.filter(tipo_usuario = 4).count()
    
    return render(
        request, 'home/dashboard.html',
        {
            'admin' : admin,
            'artistas' : artistas,
            'organizadores' : organizadores,
            'asistentes' : asistentes
        }        
    )

#Administradores
#listadoAdministradores
def listadoAdministradores(request):
    administradores = Usuario.objects.filter(tipo_usuario=TipoUsuario.objects.get(id_tipo_usuario=1))
    return render(request, 'Usuarios/listadoAdministradores.html', {'administradores':administradores})

#crearAdministrador
def crearAdministrador(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=1)
    
    usuario = Usuario.objects.create(ci=ci, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, correo=correo, contraseña=contraseña, tipo_usuario=tipo_usuario)
    return redirect('listadoAdministradores')
#Listado por id
def listadoAdministradorID(request, id):
    administrador = get_object_or_404(Usuario, ci=id)
    data = {
        'id_usuario': administrador.id_usuario,
        'ci': administrador.ci,
        'nombre': administrador.nombre,
        'apellido': administrador.apellido,
        'fecha_nacimiento': administrador.fecha_nacimiento.strftime('%Y-%m-%d'),
        'correo': administrador.correo,
        'contraseña': administrador.contraseña,
    }
    return JsonResponse(data)

#actulaizarAdministradores
def actualizar_administrador(request):
    id = request.POST.get('id_act')
    ci = request.POST.get('ci_act')
    nombre = request.POST.get('nombre_act')
    apellido = request.POST.get('apellido_act')
    fecha_nacimiento = request.POST.get('fecha_nacimiento_act')
    correo = request.POST.get('correo_act')
    contraseña = request.POST.get('contraseña_act')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=1)
        
    usuario = get_object_or_404(Usuario, id_usuario=id)

    usuario.ci = ci
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.fecha_nacimiento = fecha_nacimiento
    usuario.correo = correo
    usuario.contraseña = contraseña
    usuario.tipo_usuario = tipo_usuario

    usuario.save()
    
    return redirect('listadoAdministradores')



#Clientes
#listadoClientes
def listadoClientes(request):
    clientes = Usuario.objects.filter(tipo_usuario=TipoUsuario.objects.get(id_tipo_usuario=4))
    return render(request, 'Usuarios/listadoClientes.html', {'clientes':clientes})

#crearCliente
def crearCliente(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=4)
    
    usuario = Usuario.objects.create(ci=ci, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, correo=correo, contraseña=contraseña, tipo_usuario=tipo_usuario)
    return redirect('listadoClientes')

#Artista
#listadoArtista
def listadoArtista(request):
    artista = Usuario.objects.filter(tipo_usuario=TipoUsuario.objects.get(id_tipo_usuario=2))
    return render(request, 'Usuarios/listadoArtistas.html', {'artista':artista})

#crearCliente
def crearArtista(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    biografia = request.POST.get('biografia')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=4)
    
    usuario = Usuario.objects.create(
        ci = ci, 
        nombre = nombre, 
        apellido = apellido, 
        fecha_nacimiento = fecha_nacimiento, 
        correo = correo,
        contraseña = contraseña, 
        tipo_usuario=tipo_usuario
    )
    
    id = Usuario.objects.get(ci = ci)
    
    Biografía.objects.create(
        biografia = biografia,
        usuario = id
    )
    
    return redirect('listadoArtista')

def listadoArtistaID(request, id):
    administrador = get_object_or_404(Usuario, ci=id)
    data = {
        'id_usuario': administrador.id_usuario,
        'ci': administrador.ci,
        'nombre': administrador.nombre,
        'apellido': administrador.apellido,
        'fecha_nacimiento': administrador.fecha_nacimiento.strftime('%Y-%m-%d'),
        'correo': administrador.correo,
        'contraseña': administrador.contraseña,
    }
    return JsonResponse(data)

#actulaizarAdministradores
def actualizar_artista(request):
    id = request.POST.get('id_act')
    ci = request.POST.get('ci_act')
    nombre = request.POST.get('nombre_act')
    apellido = request.POST.get('apellido_act')
    fecha_nacimiento = request.POST.get('fecha_nacimiento_act')
    correo = request.POST.get('correo_act')
    contraseña = request.POST.get('contraseña_act')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=1)
        
    usuario = get_object_or_404(Usuario, id_usuario=id)

    usuario.ci = ci
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.fecha_nacimiento = fecha_nacimiento
    usuario.correo = correo
    usuario.contraseña = contraseña
    usuario.tipo_usuario = tipo_usuario

    usuario.save()
    
    return redirect('listadoArtista')


#Organizadores
#listadoOrganizadores
def listadoOrganizadores(request):
    organizador = Usuario.objects.filter(tipo_usuario=TipoUsuario.objects.get(id_tipo_usuario=3))
    return render(request, 'Usuarios/listadoOrganizadores.html', {'organizador':organizador})

#crearOrganizadores
def crearOrganizadores(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=3)
    
    usuario = Usuario.objects.create(
        ci = ci, 
        nombre = nombre, 
        apellido = apellido, 
        fecha_nacimiento = fecha_nacimiento, 
        correo = correo,
        contraseña = contraseña, 
        tipo_usuario=tipo_usuario
    )
    
    return redirect('listadoClientes')

def festival_list(request):
    festivales = Festival.objects.all()
    return render(request, 'Festivales/listarFestival.html', {'festivales': festivales})

def crear_festival(request):
    # Obtener los datos del formulario manualmente
    nombre = request.POST.get('nombre')
    ubicacion = request.POST.get('ubicacion')
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_fin = request.POST.get('fecha_fin')
    descripcion = request.POST.get('descripcion')
    usuario_id = random.randint(1, 1000)
    
    id = Usuario.objects.get(id_usuario = usuario_id)
    
    Festival.objects.create(
        nombre=nombre,
        ubicacion=ubicacion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        descripcion=descripcion,
        usuario=id
    )
    return redirect('crear_festival')