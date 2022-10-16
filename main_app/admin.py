from django.contrib import admin
from .models import Task, Tasklist, User

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'completed')

class TasklistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tasklist._meta.get_fields() if not field.many_to_many]

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')

admin.site.register(Task, TaskAdmin)
admin.site.register(Tasklist, TasklistAdmin)
