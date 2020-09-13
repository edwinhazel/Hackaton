from django.urls import path, include

from . import views

app_name = 'gestor'

urlpatterns = [
    path('salon/crear/', views.SalonCreateView.as_view(), name='create_salon'),
    path('salon/<int:clave>/', views.SalonDetailView.as_view(), name='detail_salon'),
    path('salon/<int:clave>/actualizar/', views.SalonUpdateView.as_view(), name='update_salon'),
]

# URLs para la alta, baja y cambio de estudiante
urlpatterns += [
    path('salon/<int:clave>/estudiante/crear/', views.EstudianteCreateView.as_view(), name='create_estudiante'),
    path('salon/<int:clave>/estudiante/<int:id_estudiante>/', views.EstudianteUpdateView.as_view(), name='update_estudiante'),
]

# URLs para la alta, baja y cambio de clase
urlpatterns += [
    path('salon/<int:clave>/clase/crear/', views.ClaseCreateView.as_view(), name='create_clase'),
    path('salon/<int:clave>/clase/<int:num_clase>/', views.ClaseUpdateView.as_view(), name='update_clase'),
]