from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

# there are so many features of django which i have used for this project and one of these are 
# viewsets for crud operations and it ultimately helps for writing optimised code 

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
