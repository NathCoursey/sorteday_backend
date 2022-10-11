from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Task, Tasklist
from rest_framework import viewsets
from .serializers import TaskSerializer

class Home(View):
    def get(self, request):
        return HttpResponse("SorteDay Home")

class About(View):
    def get(self, request):
        return HttpResponse("SorteDay About")

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


