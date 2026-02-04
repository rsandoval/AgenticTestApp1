from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from training.models import TrainingProcess, Enrollment
from accounts.models import User


@login_required
def index(request):
    active_processes = TrainingProcess.objects.filter(status='active').count()
    student_count = User.objects.filter(role='student').count()
    total_enrollments = Enrollment.objects.count()
    completed_enrollments = Enrollment.objects.filter(status='completed').count()
    completion_rate = 0
    if total_enrollments:
        completion_rate = (completed_enrollments / total_enrollments) * 100
    context = {
        'active_processes': active_processes,
        'student_count': student_count,
        'completion_rate': round(completion_rate, 2),
    }
    return render(request, 'dashboard/index.html', context)
