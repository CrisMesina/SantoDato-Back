"""
URL configuration for SantoDatos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pymes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.formLogin),
    path('contacto', views.mostrarContacto),
    path('contactanos', views.mostrarContactoNoLogin),
    path('registro',views.mostrarRegistro),
    path('isRegister', views.crearUsuario),
    path('isLogin', views.iniciarSesion),
    path("logueado",views.mostrarIndexLogueado),
    path("cerrar", views.cerrarSesion),
    path('servicios', views.mostrarServicios),
    path('comida', views.mostrarComida),
    path('hospedajes', views.mostrarAlojamientos),
    path('m_pymes', views.mostrarPymes),
    path('pymes', views.registarPymes)
    
]
