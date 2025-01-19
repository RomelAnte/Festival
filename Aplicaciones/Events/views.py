from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Festival, User, TypeUser, Literature
import random

# Create your views here.

def index(request):
    return render(request, 'Pages/home.html')

def login(request):
    return render(request, 'Pages/login.html')

def inicio(request):
    admin = User.objects.filter(type_user = 1).count()
    artistas = User.objects.filter(type_user = 2).count()
    organizadores = User.objects.filter(type_user = 3).count()
    asistentes = User.objects.filter(type_user = 4).count()
    
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
    administrators = User.objects.filter(type_user_id=1)
    return render(request, 'Usuarios/listadoAdministradores.html', {'administrators':administrators})

#crearAdministrador
def crearAdministrador(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TypeUser.objects.get(id_type = 1)
    
    usuario = User.objects.create(ci = ci, name = nombre, last_name = apellido, birthdate = fecha_nacimiento, email = correo, password = contraseña, type_user = tipo_usuario)
    return redirect('listadoAdministradores')
#Listado por id
def listadoAdministradorID(request, id):
    administrador = get_object_or_404(User, ci=id)
    data = {
        'id_use': administrador.id_use,
        'ci': administrador.ci,
        'name': administrador.name,
        'last_name': administrador.last_name,
        'birthdate': administrador.birthdate.strftime('%Y-%m-%d'),
        'email': administrador.email,
        'password': administrador.password,
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
    tipo_usuario = TypeUser.objects.get(id_type=1)
        
    user = get_object_or_404(User, id_use=id)

    user.ci = ci
    user.name = nombre
    user.last_name = apellido
    user.birthdate = fecha_nacimiento
    user.email = correo
    user.password = contraseña
    user.type_user = tipo_usuario

    user.save()
    
    return redirect('listadoAdministradores')



#Clientes
#listadoClientes
def listadoClientes(request):
    clients = User.objects.filter(type_user=TypeUser.objects.get(id_type=4))
    return render(request, 'Usuarios/listadoClientes.html', {'clients':clients})

#crearCliente
def crearCliente(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TypeUser.objects.get(id_type=4)
    
    usuario = User.objects.create(ci = ci, name = nombre, last_name = apellido, birthdate = fecha_nacimiento, email = correo, password = contraseña, type_user = tipo_usuario)
    return redirect('listadoClientes')

#Artista
#listadoArtista
def listadoArtista(request):
    artista = User.objects.filter(tipo_usuario=TypeUser.objects.get(id_tipo_usuario=2))
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
    tipo_usuario = TypeUser.objects.get(id_tipo_usuario=4)
    
    usuario = User.objects.create(
        ci = ci, 
        nombre = nombre, 
        apellido = apellido, 
        fecha_nacimiento = fecha_nacimiento, 
        correo = correo,
        contraseña = contraseña, 
        tipo_usuario=tipo_usuario
    )
    
    id = User.objects.get(ci = ci)
    
    Literature.objects.create(
        biografia = biografia,
        usuario = id
    )
    
    return redirect('listadoArtista')

def listadoArtistaID(request, id):
    administrador = get_object_or_404(User, ci=id)
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
    tipo_usuario = TypeUser.objects.get(id_tipo_usuario=1)
        
    usuario = get_object_or_404(User, id_usuario=id)

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
    organizador = User.objects.filter(tipo_usuario=TypeUser.objects.get(id_tipo_usuario=3))
    return render(request, 'Usuarios/listadoOrganizadores.html', {'organizador':organizador})

#crearOrganizadores
def crearOrganizadores(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TypeUser.objects.get(id_tipo_usuario=3)
    
    usuario = User.objects.create(
        ci = ci, 
        nombre = nombre, 
        apellido = apellido, 
        fecha_nacimiento = fecha_nacimiento, 
        correo = correo,
        contraseña = contraseña, 
        tipo_usuario=tipo_usuario
    )
    
    return redirect('listadoOrganizadores')

def eliminarUsuario(request, id):
    usuario = get_object_or_404(User, id_use=id)
    usuario.delete()
    return redirect('listadoArtista')


def festival_list(request):
    festivals = Festival.objects.all()
    return render(request, 'Festivals/listFestival.html', {'festivals': festivals})

def crear_festival(request):
    # Obtener los datos del formulario manualmente
    nombre = request.POST.get('name')
    ubicacion = request.POST.get('location')
    fecha_inicio = request.POST.get('start_date')
    fecha_fin = request.POST.get('end_date')
    descripcion = request.POST.get('description')
    usuario_id = random.randint(1, 1000)

    Festival.objects.create(
        name = nombre,
        address = ubicacion,
        startDate = fecha_inicio,
        endDate = fecha_fin,
        description = descripcion,
        user_id = usuario_id
    )
    return redirect('festival_list')

def listadoFestivalID(request, id):
    festival = get_object_or_404(Festival, id_fes=id)
    data = {
        'id_festival': festival.id_fes,
        'name_act': festival.name,
        'location_act': festival.address,
        'start_date_act': festival.startDate.strftime('%Y-%m-%d'),
        'end_date_act': festival.endDate.strftime('%Y-%m-%d'),
        'description_act': festival.description,
    }
    return JsonResponse(data)

#actulaizarAdministradores
def actualizar_festival(request):
    id = request.POST.get('id_act')
    name = request.POST.get('name_act')
    location = request.POST.get('location_act')
    start = request.POST.get('start_date_act')
    end = request.POST.get('end_date_act')
    descripction = request.POST.get('description_act')
        
    festival = get_object_or_404(Festival, id_fes=id)
    
    festival.name = name
    festival.address = location
    festival.startDate = start
    festival.endDate = end
    festival.description = descripction

    festival.save()
    
    return redirect('festival_list')

def deleteFestival(request, id):
    festival = get_object_or_404(Festival, id_fes=id)
    festival.delete()
    
    return redirect('festival_list')