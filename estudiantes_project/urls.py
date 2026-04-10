from django.contrib import admin
from django.urls import path, include
from estudiantes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', include('estudiantes.urls')),
    path('', views.inicio, name='inicio'),  # Landing page en la raíz
]