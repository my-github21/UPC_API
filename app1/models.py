

from django.contrib.auth.models import User  # this is default admin user for creating user for our project
from django.db import models


 #craeting client model for client data
 
class Client(models.Model):    
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    
#creating project model for project info
class Project(models.Model):    
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
