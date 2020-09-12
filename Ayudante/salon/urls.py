from django.urls import path, include

from . import views

app_name = 'salon'

urlpatterns = [
    path('create/', views.SalonCreateView.as_view(), name='create_salon'),
]