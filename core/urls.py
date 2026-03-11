from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('proyecto/<slug:slug>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('contacto/', views.contacto, name='contacto'),
]
