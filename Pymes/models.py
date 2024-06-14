from django.db import models

# Create your models here.

class Pymes(models.Model):
    nombre = models.TextField(max_length=75)
    contacto = models.TextField(max_length=15)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return str(self.nombre) + " - " + str(self.contacto)+ " + " + str(self.descripcion)     

class Usuarios(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=30)

    def __str__(self):
        return str(self.name) + " - " + str(self.email) + " - " + str(self.password)
    


    