from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    date = models.DateField(default=datetime.today)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Tasklist(models.Model):
    title = models.CharField(max_length=150)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.title



