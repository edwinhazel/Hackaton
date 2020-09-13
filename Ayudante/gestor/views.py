from django.shortcuts import render
from django.urls import reverse

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

    def get_success_url(self, **kwargs):
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

class SalonDetailView(DetailView, LoginRequiredMixin):
    template_name = "SalonDetail.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Salon
    pk_url_kwarg='clave'
    context_object_name = 'salon'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        salon = Salon.objects.get(clave=self.kwargs['clave'])
        print(self.kwargs['clave'])
        context['estudiantes'] = Estudiante.objects.filter(salon=salon)
        context['clases'] = Clase.objects.filter(salon=salon)
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
    
    def get_success_url(self, **kwargs):
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

class EstudianteCreateView(CreateView, LoginRequiredMixin):
    template_name = "EstudianteCreate.html"
    login_url = 'login/'
    model = Estudiante
    form_class = EstudianteCreateForm

    def form_valid(self, form):
        form.instance.salon = Salon.objects.get(clave=self.kwargs['clave'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

class EstudianteUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "EstudianteUpdate.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Estudiante
    pk_url_kwarg = 'id_estudiante'
    form_class = EstudianteUpdateForm

    def get_success_url(self, **kwargs):
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

    def get_form_kwargs(self):
        kwargs = super(EstudianteUpdateView, self).get_form_kwargs()
        kwargs.update({'clave': self.kwargs['clave']})
        return kwargs

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
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

class ClaseUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "ClaseUpdate.html"
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Clase
    pk_url_kwarg = 'num_clase'
    form_class = ClaseUpdateForm

    def get_success_url(self, **kwargs):
        return reverse('gestor:detail_salon', kwargs={'clave': self.kwargs['clave']})

    def get_form_kwargs(self):
        kwargs = super(ClaseUpdateView, self).get_form_kwargs()
        kwargs.update({'clave': self.kwargs['clave']})
        return kwargs
