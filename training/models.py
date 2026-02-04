from django.db import models
from accounts.models import User


class TrainingProcess(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    target_completion_rate = models.FloatField(default=100.0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_processes')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    process = models.ForeignKey(TrainingProcess, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'process')

    def __str__(self):
        return f"{self.user.email} - {self.process.name}"
