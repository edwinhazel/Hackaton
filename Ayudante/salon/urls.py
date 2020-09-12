from django.urls import path, include

from . import views

app_name = 'salon'

urlpatterns = [
    path('create/', views.SalonCreateView.as_view(), name='create_salon'),
    path('<int:clave>/update/', views.SalonUpdateView.as_view(), name='update_salon'),
]

# URLs para la alta, baja y cambio de estudiante
urlpatterns += [
    path('<int:clave>/estudiante/create/', views.EstudianteCreateView.as_view(), name='create_estudiante'),
    path('<int:clave>/estudiante/<int:id_estudiante>/', views.EstudianteUpdateView.as_view(), name='update_estudiante'),
]