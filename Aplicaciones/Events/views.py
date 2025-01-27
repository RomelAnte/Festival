from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Festival, User, TypeUser, Literature, Licence, Audit
import random

class GlobalVariables:
    typeUse = ''

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
    GlobalVariables.typeUse = 'listadoAdministradores'
    administrators = User.objects.filter(type_user_id=1)
    return render(request, 'Usuarios/listadoAdministradores.html', {'administrators':administrators})

#crearAdministrador
def crearAdministrador(request):
    ci = request.POST.get('ci')    
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoAdministradores')
    
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    
    correo = request.POST.get('correo')
    if User.objects.filter(email=correo).exists():
        return redirect('listadoAdministradores')
    
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
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoAdministradores')
    
    nombre = request.POST.get('nombre_act')
    apellido = request.POST.get('apellido_act')
    fecha_nacimiento = request.POST.get('fecha_nacimiento_act')
    correo = request.POST.get('correo_act')
    if User.objects.filter(email=correo).exists():
        return redirect('listadoAdministradores')
    
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
    GlobalVariables.typeUse = 'listadoClientes'
    clients = User.objects.filter(type_user=TypeUser.objects.get(id_type=4))
    return render(request, 'Usuarios/listadoClientes.html', {'clients':clients})

#crearCliente
def crearCliente(request):
    ci = request.POST.get('ci')
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoClientes')
    
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    if User.objects.filter(email=correo).exists():
        return redirect('listadoClientes')
    
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TypeUser.objects.get(id_type=4)
    
    usuario = User.objects.create(
        ci = ci, 
        name = nombre, 
        last_name = apellido, 
        birthdate = fecha_nacimiento, 
        email = correo, 
        password = contraseña, 
        type_user = tipo_usuario
    )
    
    return redirect('listadoClientes')

#Artista
#listadoArtista
def listadoArtista(request):
    GlobalVariables.typeUse = 'listadoArtista'
    artista = User.objects.filter(type_user=2)
    return render(request, 'Usuarios/listadoArtistas.html', {'artista':artista})

#crearCliente
def crearArtista(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoArtista')
    
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    if User.objects.filter(correo=correo).exists():
        return redirect('listadoArtista')
    
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
    single = get_object_or_404(User, ci=id)
    data = {
        'id_use': single.id_use,
        'ci': single.ci,
        'name': single.name,
        'last_name': single.last_name,
        'birthdate': single.birthdate.strftime('%Y-%m-%d'),
        'email': single.email,
        'password': single.password,
    }
    return JsonResponse(data)

#actulaizarAdministradores
def actualizar_artista(request):
    id = request.POST.get('id_act')
    ci = request.POST.get('ci_act')
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoArtista')
    
    nombre = request.POST.get('nombre_act')
    apellido = request.POST.get('apellido_act')
    fecha_nacimiento = request.POST.get('fecha_nacimiento_act')
    correo = request.POST.get('correo_act')
    if User.objects.filter(email=correo).exists():
        return redirect('listadoArtista')
    
    contraseña = request.POST.get('contraseña_act')
    tipo_usuario = TypeUser.objects.get(id_tipo_usuario=1)
        
    usuario = get_object_or_404(User, id_usuario=id)

    usuario.ci = ci
    usuario.name = nombre
    usuario.last_name = apellido
    usuario.birthdate = fecha_nacimiento
    usuario.email = correo
    usuario.password = contraseña
    usuario.type_user = tipo_usuario

    usuario.save()
    
    return redirect('listadoArtista')


#Organizadores
#listadoOrganizadores
def listadoOrganizadores(request):
    GlobalVariables.typeUse = 'listadoOrganizadores'
    organizador = User.objects.filter(type_user = 3)
    return render(request, 'Usuarios/listadoOrganizadores.html', {'organizador':organizador})

#crearOrganizadores
def crearOrganizadores(request):
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    if User.objects.filter(ci=ci).exists():
        return redirect('listadoOrganizadores')
    
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    correo = request.POST.get('correo')
    if User.objects.filter(correo=correo).exists():
        return redirect('listadoOrganizadores')
    
    contraseña = request.POST.get('contraseña')
    tipo_usuario = TypeUser.objects.get(id_tipo_usuario=3)
    
    usuario = User.objects.create(
        ci = ci, 
        name = nombre, 
        last_name = apellido, 
        birthdate = fecha_nacimiento, 
        email = correo,
        password = contraseña, 
        type_user = tipo_usuario
    )
    
    return redirect('listadoOrganizadores')

# listado por id
def listadoOrganizadorID(request, id):
    organizador = get_object_or_404(User, id_use=id)
    data = {
        'id_usuario': organizador.id_use,
        'ci': organizador.ci,
        'nombre': organizador.name,
        'apellido': organizador.last_name,
        'fecha_nacimiento': organizador.birthdate.strftime('%Y-%m-%d'),
        'correo': organizador.email,
        'contraseña': organizador.password,
    }
    return JsonResponse(data)

#actulaizarOrganizadores
def actualizar_organizador(request):
    id = request.POST.get('id_act')
    ci = request.POST.get('ci_act')    
    nombre = request.POST.get('nombre_act')
    apellido = request.POST.get('apellido_act')
    fecha_nacimiento = request.POST.get('fecha_nacimiento_act')
    correo = request.POST.get('correo_act')    
    contraseña = request.POST.get('contraseña_act')
    tipo_usuario = TypeUser.objects.get(id_type = 3)
        
    usuario = get_object_or_404(User, id_use = id)

    usuario.ci = ci
    usuario.name = nombre
    usuario.last_name = apellido
    usuario.birthdate = fecha_nacimiento
    usuario.email = correo
    usuario.password = contraseña
    usuario.type_user = tipo_usuario

    usuario.save()
    
    return redirect('listadoOrganizadores')

def eliminarUsuario(request, id):
    usuario = get_object_or_404(User, id_use=id)
    usuario.delete()
    return redirect(GlobalVariables.typeUse)


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

def listLicences(request):
    licences = Licence.objects.all()
    return render(request, 'Licences/listLicences.html', {'licences': licences})

def createLicence(request):
    type = request.POST.get('licence')
    price = request.POST.get('price')
    acronnym = request.POST.get('acronnym')
    
    Licence.objects.create(
        type = type,
        price = price,
        acronnym = acronnym
    )
    
    return redirect('listLicences')

def listLicencesID(request, id):
    licence = get_object_or_404(Licence, id_lic=id)
    data = {
        'id_lic': licence.id_lic,
        'type': licence.type,
        'price': licence.price,
        'acronnym': licence.acronnym,
        'status': licence.status
    }
    return JsonResponse(data)

def updateLicence(request):
    id = request.POST.get('id_act')
    type = request.POST.get('licence_act')
    price = request.POST.get('price_act')
    acronnym = request.POST.get('acronnym_act')
    is_active= request.POST.get('status_act')
    status = True if is_active == "true" else False
    
    licence = get_object_or_404(Licence, id_lic=id)
    
    licence.type = type
    licence.price = price
    licence.acronnym = acronnym
    licence.status = status
    
    licence.save()
    
    return redirect('listLicences')

def deleteLicence(request, id):
    licence = get_object_or_404(Licence, id_lic=id)
    licence.delete()
    
    return redirect('listLicences')

def listAudits(request):
    audits = Audit.objects.all()
    users = User.objects.filter(type_user_id=4)
    return render(request, 'Audits/listAudits.html', {'audits': audits, 'users': users})

def createAudit(request):
    date = request.POST.get('date')
    description = request.POST.get('description')
    gender = request.POST.get('gender')
    user_id = request.POST.get('user')
    
    Audit.objects.create(
        date = date,        
        description = description,
        gender = gender,
        user_id = user_id
    )
    
    return redirect('listAudits')

def listAuditsID(request, id):
    audit = get_object_or_404(Audit, id_audit=id)
    data = {
        'id_audit': audit.id_audit,
        'date': audit.date,
        'description': audit.description,
        'gender': audit.gender,
        'user': audit.user.id_use
    }
    
    return JsonResponse(data)

def updateAudit(request):
    id = request.POST.get('id_act')
    date = request.POST.get('date_act')
    description = request.POST.get('description_act')
    gender = request.POST.get('gender_act')
    user_id = request.POST.get('user_act')
    
    audit = get_object_or_404(Audit, id_audit=id)
    
    audit.date = date
    audit.description = description
    audit.gender = gender
    audit.user_id = user_id
    
    audit.save()
    return redirect('listAudits')
    

def deleteAudit(request, id):
    audit = get_object_or_404(Audit, id_audit=id)
    audit.delete()
    
    return redirect('listAudits')