from django.shortcuts import render

from .models import Salon
from .forms import SalonCreateForm, SalonUpdateForm

from .models import Estudiante
from .forms import EstudianteCreateForm, EstudianteUpdateForm

from .models import Clase
from .forms import ClaseCreateForm, ClaseUpdateForm

from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class SalonCreateView(CreateView, LoginRequiredMixin):
    template_name = 'SalonCreate.html'
    login_url = 'login/'
    model = Salon
    form_class = SalonCreateForm

class SalonUpdateView(UpdateView, SingleObjectMixin, LoginRequiredMixin):
    template_name = 'SalonCreate.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Salon
    pk_url_kwarg='clave'
    form_class = SalonUpdateForm

class EstudianteCreateView(CreateView, LoginRequiredMixin):
    template_name = 'EstudianteCreate.html'
    login_url = 'login/'
    model = Estudiante
    form_class = EstudianteCreateForm

class EstudianteUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'EstudianteUpdate.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Estudiante
    form_class = EstudianteUpdateForm

class ClaseCreateView(CreateView, LoginRequiredMixin):
    template_name = 'ClaseCreate.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Clase
    form_class = ClaseCreateForm

class ClaseUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'ClaseUpdate.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Clase
    form_class = ClaseUpdateForm
