from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Time in minutes")

    def __str__(self):
        return self.title


# Create your models here.
