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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(SalonCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        new_salon = super(SalonCreateForm, self).save(commit=False)
        new_salon.id_user = self.user
        new_salon.save()

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
            'nombre',
            'email',
        }
        exclude = ['salon',]
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo',
        }

class EstudianteUpdateForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = {
            'nombre',
            'email',
        }
        exclude = ['salon',]
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo',
        }

    def __init__(self, *args, **kwargs):
        self.salon = kwargs.pop('clave')
        super(EstudianteUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        new_salon = super(EstudianteUpdateForm, self).save(commit=False)
        new_salon.salon = self.salon
        new_salon.save()

class ClaseCreateForm(ModelForm):
    class Meta:
        model = Clase
        fields = {
            'nombre',
            'descripcion',
            'audio',
        }
        exclude = ['salon',]
        labels = {
            'nombre': 'Nombre de clase',
            'descripcion': 'Descripción',
            'audio': 'Audio',
        }

class ClaseUpdateForm(ModelForm):
    class Meta:
        model = Clase
        fields = {
            'nombre',
            'descripcion',
        }
        exclude = ['salon',]
        labels = {
            'nombre': 'Nombre de clase',
            'descripcion': 'Descripción',
        }

    def __init__(self, *args, **kwargs):
        self.salon = kwargs.pop('clave')
        super(ClaseUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        new_salon = super(ClaseUpdateForm, self).save(commit=False)
        new_salon.salon = self.salon
        new_salon.save()