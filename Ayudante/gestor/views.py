from django.shortcuts import render

from .models import Salon
from .forms import SalonCreateForm, SalonUpdateForm

from .models import Estudiante
from .forms import EstudianteCreateForm, EstudianteUpdateForm

from .models import Clase
from .forms import ClaseCreateForm, ClaseUpdateForm

from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class SalonCreateView(CreateView, LoginRequiredMixin):
    template_name = "SalonCreate.html"
    login_url = 'login/'
    model = Salon
    form_class = SalonCreateForm

    def get_form_kwargs(self):
        kwargs = super(SalonCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class SalonDetailView(DetailView, LoginRequiredMixin):
    template_name = "SalonDetail.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Salon
    pk_url_kwarg='clave'
    context_object_name = 'salon'
    
    def get_context_data(self, **kwargs):
        context = context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.get(salon=kwargs['clave'])
        context['clases'] = Clase.objects.get(salon=kwargs['clave'])
        return context

class SalonUpdateView(UpdateView, SingleObjectMixin, LoginRequiredMixin):
    template_name = "SalonUpdate.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Salon
    pk_url_kwarg='clave'
    context_object_name = 'salon'
    form_class = SalonUpdateForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        print(self.get_object())

class EstudianteCreateView(CreateView, LoginRequiredMixin):
    template_name = "EstudianteCreate.html"
    login_url = 'login/'
    model = Estudiante
    form_class = EstudianteCreateForm

    def form_valid(self, form):
        form.instance.salon = Salon.objects.get(clave=self.kwargs['clave'])
        return super().form_valid(form)

class EstudianteUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "EstudianteUpdate.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Estudiante
    form_class = EstudianteUpdateForm

class ClaseCreateView(CreateView, LoginRequiredMixin):
    template_name = "ClaseCreate.html"
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Clase
    form_class = ClaseCreateForm

    def form_valid(self, form):
        form.instance.salon = Salon.objects.get(clave=self.kwargs['clave'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('gestor:create_clase', kwargs={'clave': self.kwargs['clave']})

class ClaseUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "ClaseUpdate.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Clase
    form_class = ClaseUpdateForm
