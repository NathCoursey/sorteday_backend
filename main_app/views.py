from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Task, Tasklist
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class Home(View):
    def get(self, request):
        return HttpResponse("SorteDay Home")

class About(View):
    def get(self, request):
        return HttpResponse("SorteDay About")

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer