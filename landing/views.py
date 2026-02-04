from django.shortcuts import render


def landing(request):
    # Contenido de ejemplo para la landing page
    features = [
        {'title': 'Gestión de procesos', 'desc': 'Crear y seguir procesos de capacitación.'},
        {'title': 'Registro de estudiantes', 'desc': 'Inscripción y administración de estudiantes.'},
        {'title': 'Rendimiento y progreso', 'desc': 'Seguimiento de tasas de finalización.'},
    ]
    return render(request, 'landing/index.html', {'features': features})
