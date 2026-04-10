from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estudiante

# Vista para la página de inicio
def inicio(request):
    return render(request, 'estudiantes/inicio.html')

# Vista para listar todos los estudiantes (READ)
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

# Vista para crear un estudiante (CREATE)
def crear_estudiante(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        programa = request.POST.get('programa')
        semestre = request.POST.get('semestre')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        activo = request.POST.get('activo') == 'on'
        
        Estudiante.objects.create(
            codigo=codigo,
            nombre=nombre,
            apellido=apellido,
            email=email,
            programa=programa,
            semestre=semestre,
            fecha_ingreso=fecha_ingreso,
            activo=activo
        )
        
        messages.success(request, 'Estudiante creado exitosamente!')
        return redirect('lista_estudiantes')
    
    return render(request, 'estudiantes/crear.html')

# Vista para ver detalle de un estudiante
def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})

# Vista para actualizar un estudiante (UPDATE)
def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    
    if request.method == 'POST':
        estudiante.codigo = request.POST.get('codigo')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.email = request.POST.get('email')
        estudiante.programa = request.POST.get('programa')
        estudiante.semestre = request.POST.get('semestre')
        estudiante.fecha_ingreso = request.POST.get('fecha_ingreso')
        estudiante.activo = request.POST.get('activo') == 'on'
        estudiante.save()
        
        messages.success(request, 'Estudiante actualizado exitosamente!')
        return redirect('lista_estudiantes')
    
    return render(request, 'estudiantes/actualizar.html', {'estudiante': estudiante})

# Vista para eliminar un estudiante (DELETE)
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado exitosamente!')
        return redirect('lista_estudiantes')
    
    return render(request, 'estudiantes/eliminar.html', {'estudiante': estudiante})