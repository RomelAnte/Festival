from django.shortcuts import render, redirect
from .models import Usuario, TipoUsuario
# Create your views here.

def index(request):
    return render(request, 'Pages/home.html')

def login(request):
    return render(request, 'Pages/login.html')

def inicio(request):
    return render(request, 'home/dashboard.html')

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
