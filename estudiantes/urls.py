from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('<int:pk>/actualizar/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('<int:pk>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
]