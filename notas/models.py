from django.db import models
from django.utils import timezone
from django.contrib import admin

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    dpi = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        respuesta = str(self.dpi) + ' - ' +self.nombre
        return respuesta

class Materia(models.Model):
    materia = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor)

    def __str__(self):
        respuesta = self.materia
        return respuesta

class Grado(models.Model):
    grado = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    materias = models.ManyToManyField(Materia, through='Pensum')

    def __str__(self):
        respuesta = self.grado + ' - ' + self.seccion
        return respuesta

class Pensum(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class PensumInLine(admin.TabularInline):
    model = Pensum
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (PensumInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (PensumInLine,)

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    grado = models.ForeignKey(Grado)

    def __str__(self):
        respuesta = self.nombre
        return respuesta
