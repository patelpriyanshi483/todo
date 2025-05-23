from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    estimated_time = models.IntegerField(null=True, blank=True)
    deadline = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def is_overdue(self):
        return timezone.now() > self.deadline

    def __str__(self):
        return self.title
