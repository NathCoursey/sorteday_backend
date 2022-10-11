from django.contrib import admin
from .models import Task, Tasklist

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'completed')

class TasklistAdmin(admin.ModelAdmin):
    list_display = ('title', 'tasks')

admin.site.register(Task, TaskAdmin)
admin.site.register(Tasklist, TasklistAdmin)
