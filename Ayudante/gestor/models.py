from django.db import models

from django.contrib.auth.models import User

DESCRIPTIONLESS = 'Sin Descripción'
NAMELESS = 'Sin Nombre'

class Salon(models.Model):
    clave = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    descripcion = models.TextField(max_length=100, null=True)

    def __str__(self):
        return "clave:%d id_user:%s" % (self.clave, self.user)

class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    salon = models.ForeignKey(
        Salon, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.TextField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return "id_user:%d clave_salon:%s" % (self.id_estudiante, self.salon)


class Clase(models.Model):
    id_clase = models.IntegerField(primary_key=True)
    salon = models.ForeignKey(
        Salon,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    nombre = models.TextField(null=False, default=NAMELESS)
    descripcion = models.TextField(null=False, default=DESCRIPTIONLESS)
    audio = models.FileField(upload_to='audios/', null=True)

    def __str__(self):
        return "id_clase:%d clave_salon:%s" % (self.id_clase, self.clave_salon)
