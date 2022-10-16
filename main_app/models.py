from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    date = models.DateField(default=datetime.today)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Tasklist(models.Model):
    title = models.CharField(max_length=150)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.title




