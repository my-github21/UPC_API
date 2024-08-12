from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet


# i have used Routers for automatically generate URL patterns for the
# standard actions that your viewsets support (e.g., list, create, retrieve, update, delete).

router = DefaultRouter()
router.register(r'clients', ClientViewSet)  #this is for client related requests
router.register(r'projects', ProjectViewSet) #this is for project related requests

urlpatterns = [
    path('', include(router.urls)),
]
