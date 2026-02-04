from django.urls import path
from .views import list_processes

urlpatterns = [
    path('processes/', list_processes, name='processes'),
]
