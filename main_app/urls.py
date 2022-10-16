from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet, TaskView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskView)
urlpatterns = [
   path('', include(router.urls)),
]