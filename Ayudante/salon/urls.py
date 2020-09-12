from django.urls import path, include

from . import views

app_name = 'salon'

urlpatterns = [
    path('crear/', views.SalonCreateView.as_view(), name='create_salon'),
    path('<int:clave>/actualizar/', views.SalonUpdateView.as_view(), name='update_salon'),
]

# URLs para la alta, baja y cambio de estudiante
urlpatterns += [
    path('<int:clave>/estudiante/crear/', views.EstudianteCreateView.as_view(), name='create_estudiante'),
    path('<int:clave>/estudiante/<int:id_estudiante>/', views.EstudianteUpdateView.as_view(), name='update_estudiante'),
]