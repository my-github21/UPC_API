# Project_Management

## Overview

This project is a Django REST Framework-based API for managing users, clients, and projects. The API allows for the registration of clients, fetching client information, editing/deleting client information, adding new projects for a client, assigning users to those projects, and retrieving projects assigned to logged-in users.

## Features

- **User Management**: Uses Django's default admin template to create/register users.
- **Client Management**: Create, retrieve, update, and delete client information.
- **Project Management**: Add new projects, assign users to projects, and retrieve projects assigned to logged-in users.

## Technical Requirements

- **Framework**: Django REST Framework (if not 'pip install rest_framework')
- **Database**: MySQL 

## Creating Superuser
- python manage.py shell
- from django.contrib.auth.models import User
- user1 = User.objects.create_user(username='Ram', password='jayshreeram')

## Urls and steps for using POST and browser
 ### POST
- **Creating client**: after runserver , 'http://127.0.0.1:8000/api/clients/' with 'POST' request.
- **Creating Project**: after runserver , 'http://127.0.0.1:8000/api/projects/' with 'POST' request.
 ### GET
- **Client information**: after runserver , 'http://127.0.0.1:8000/api/clients/' with 'GET' request.
- **Project information**: after runserver , 'http://127.0.0.1:8000/api/projects/' with 'GET' request.
- **Client information by id **: after runserver , 'http://127.0.0.1:8000/api/clients/1/' with 'Get' request it will give information for a single client according to it's id.
- **Project information by id **: after runserver , 'http://127.0.0.1:8000/api/clients/1/' with 'Get' request it will give information for a single project according to it's id.
### PUT
- **Making Changes**: after runserver , 'http://127.0.0.1:8000/api/clients/1' with 'PUT' request.
- **Making Changes**: after runserver , 'http://127.0.0.1:8000/api/projects/1' with 'PUT' request.
### DELETE
- **Deleting client**: after runserver , 'http://127.0.0.1:8000/api/clients/1' with 'DELETE' request.
- **Deleting project**: after runserver , 'http://127.0.0.1:8000/api/projects/1' with 'DELETE' request.