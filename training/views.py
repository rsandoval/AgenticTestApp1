from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TrainingProcess, Enrollment


@login_required
def list_processes(request):
    processes = TrainingProcess.objects.all()
    return render(request, 'training/process_list.html', {'processes': processes})
