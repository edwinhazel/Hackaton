from django.db import models

from django.contrib.auth.models import User

DESCRIPTIONLESS = 'Sin Descripción'
NAMELESS = 'Sin Nombre'

class Salon(models.Model):
    clave = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    descripcion = models.TextField(max_length=100, null=True)

    def __str__(self):
        return "%d" % (self.clave)

class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    salon = models.ForeignKey(
        Salon, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    nombre = models.TextField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return "<Estudiante:%d> --> %s" % (self.id_estudiante, self.salon)


class Clase(models.Model):
    num_clase = models.IntegerField(primary_key=True)
    salon = models.ForeignKey(
        Salon,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    nombre = models.TextField(default=NAMELESS)
    descripcion = models.TextField(null=False, default=DESCRIPTIONLESS)
    audio = models.FileField(upload_to='audios/', null=True)

    def __str__(self):
        return "<Clase:%d> --> %s" % (self.num_clase, self.salon)
