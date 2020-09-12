from django.forms import ModelForm

from django.contrib.auth.models import User

from .models import Salon
from .models import Estudiante
from .models import Clase

class SalonCreateForm(ModelForm):
    class Meta:
        model = Salon
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción',
        }

class SalonUpdateForm(ModelForm):
    class Meta:
        model = Salon
        fields = {
            'descripcion',
        }
        labels = {
            'descripcion': 'Descripción',
        }

class EstudianteCreateForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = {
            'name',
            'email',
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
        }

class EstudianteUpdateForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = {
            'name',
            'email',
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
        }

class ClaseCreateForm(ModelForm):
    class Meta:
        model = Clase
        fields = {
            'nombre_clase',
            'descripcion',
        }
        labels = {
            'nombre_clase': 'Nombre de clase',
            'descripcion': 'Descripción',
        }

class ClaseUpdateForm(ModelForm):
    class Meta:
        model = Clase
        fields = {
            'nombre_clase',
            'descripcion',
        }
        labels = {
            'nombre_clase': 'Nombre de clase',
            'descripcion': 'Descripción',
        }