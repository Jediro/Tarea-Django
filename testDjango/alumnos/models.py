from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    curso = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class GrupoMetal(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    albumes = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
