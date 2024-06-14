from django.shortcuts import render

from Pymes.models import Usuarios, Pymes

# Create your views here.


def index(request):
    return render(request, "index.html")

def formLogin(request):
    return render(request, 'iniciarsesion.html')

def iniciarSesion(request):
    if request.method == "POST":
        ema = request.POST["txtema"]
        pas = request.POST["txtpass"]

        comprobarLogin  = Usuarios.objects.filter(email = ema, password = pas).values()
        
        if comprobarLogin:
            request.session["estadoSesion"] = True
            request.session["idUsuario"] = comprobarLogin[0]['id']
            request.session['nomUsuario'] = ema.upper()
            
            datos = { 'nomUsuario': ema}

            return render(request, 'indexlogin.html', datos)
        else:
            datos = {
                'r2': 'ERROR DE USUARIO'
            }
            return render(request, 'iniciarsesion.html', datos)
    else:
        return render(request,'index.html')
        
def mostrarIndexLogueado(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'indexlogin.html', datos)
    else:
        return render(request,'index.html')


def mostrarContacto(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'contacto.html', datos)
    else:
        return render(request,'index.html')
    


def mostrarRegistro(request):
    return render(request, 'register.html')

def crearUsuario(request):
    if request.method == "POST":
        nom = request.POST['txtnom']
        ema = request.POST['txtema']
        pas = request.POST['txtpass']
        usu = Usuarios(name = nom, email = ema, password = pas)
        usu.save()

        return render(request, 'iniciarsesion.html')
    else:
        return render(request, 'register.html')
    


def cerrarSesion(request):
    try:

        del request.session["estadoSesion"]
        del request.session["idUsuario"]
        del request.session["nomUsuario"]

        return render(request, 'index.html')
    except:
        return render(request, 'index.html')

def mostrarServicios(request):

    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'services.html', datos)
    else:
        return render(request,'index.html')
            

def mostrarComida(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'comida.html', datos)
    else:
        return render(request,'index.html')

def mostrarAlojamientos(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'hospedajes.html', datos)
    else:
        return render(request,'index.html')

def mostrarPymes(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'pymes.html', datos)
    else:
        return render(request,'index.html')

def FormRegistroPymes(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        datos = {'nomUsuario' : nomUsuario} 
        return render(request, 'formpymes.html', datos)
    else:
        return render(request,'index.html')


def registarPymes(request):
    if request.method == "POST": 
        nom = request.POST["txtname"]
        num = request.POST["txtnum"]
        area = request.POST["txtarea"]

        comprobarPyme = Pymes.objects.filter(nombre = nom)

        if comprobarPyme:
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'r2': 'NO SE PUEDE REGISTRAR, YA EXISTE!!!'
            }
            return render(request, 'pymes.html', datos)
        else:
            pym = Pymes(nombre=nom, contacto = num, descripcion = area)
            pym.save()

            pym = Pymes.objects.all()
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'pym' : pym,
            }
            return render(request, 'pymes.html', datos)
    else:
        pym = Pymes.objects.all().values().order_by("id")
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'pym' : pym,
        }
        return render(request, 'pymes.html', datos)
