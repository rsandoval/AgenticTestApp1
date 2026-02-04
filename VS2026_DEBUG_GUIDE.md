# VS 2026 - Depurar Django con F5 (PIAmentor)
Este documento describe cómo configurar Visual Studio 2026 para depurar una aplicación Django usando F5.

Objetivo
- Abrir el proyecto Django PIAmentor desde VS 2026 y depurarlo con puntos de interrupción en Python.
- Ejecutar el servidor de desarrollo de Django desde Manage.py y depurar vistas, modelos y rutas.

Requisitos previos
- Visual Studio 2026 con workload de Python development instalado.
- Python 3.12 instalado o entorno virtual configurado (venv) con Django y dependencias necesarias.
- Archivos del repo de PIAmentor ya presentes en el entorno de VS (sln y .pyproj).

Archivos relevantes en el repo
- PIAmentor.sln (solución que incluye el proyecto Python)
- PIAmentor-Django.pyproj (proyecto Python para Django)
- manage.py (archivo de arranque de Django)
- carpeta pia/ con settings.py, urls.py, etc.

1) Preparación en VS 2026
2) Configuración de inicio (Startup) para F5
3) Puesta en marcha y depuración
4) Notas de configuración y troubleshooting
5) Consejos avanzados
- Mantén gestionadas las variables de entorno en un entorno seguro (Azure Key Vault, archivos .env en VS, o App Service settings si despliegas).
- Usa el servidor de desarrollo solo para pruebas rápidas; para producción usa Gunicorn/Nginx u otra pila compatible.
- Considera agregar un archivo README para VS 2026 con capturas y pasos de depuración.
