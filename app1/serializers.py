from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project


#i have used this serializers for  convert complex Django models or other Python objects into
# JSON, XML, or other formats that can be rendered into a response by the API.

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
