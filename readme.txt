# UPC_API

## Overview

This project is a Django REST Framework-based API for managing users, clients, and projects. The API allows for the registration of clients, fetching client information, editing/deleting client information, adding new projects for a client, assigning users to those projects, and retrieving projects assigned to logged-in users.

## Features

- **User Management**: Uses Django's default admin template to create/register users.
- **Client Management**: Create, retrieve, update, and delete client information.
- **Project Management**: Add new projects, assign users to projects, and retrieve projects assigned to logged-in users.

## Technical Requirements

- **Framework**: Django REST Framework (if not installed, run `pip install rest_framework`)
- **Database**: MySQL 

## Creating Superuser

To create a superuser, follow these steps:

1. Run the Django shell:
    ```bash
    python manage.py shell
    ```
2. Create the superuser:
    ```python
    from django.contrib.auth.models import User
    user1 = User.objects.create_user(username='Ram', password='jayshreeram')
    ```

## URLs and Steps for Using POST and Browser

### POST Requests

- **Creating a Client**: After running the server, use the following URL with a `POST` request:
  - `http://127.0.0.1:8000/api/clients/`
  
- **Creating a Project**: After running the server, use the following URL with a `POST` request:
  - `http://127.0.0.1:8000/api/projects/`

### GET Requests

- **Client Information**: After running the server, use the following URL with a `GET` request:
  - `http://127.0.0.1:8000/api/clients/`

- **Project Information**: After running the server, use the following URL with a `GET` request:
  - `http://127.0.0.1:8000/api/projects/`

- **Client Information by ID**: After running the server, use the following URL with a `GET` request to retrieve information for a specific client by its ID:
  - `http://127.0.0.1:8000/api/clients/1/`

- **Project Information by ID**: After running the server, use the following URL with a `GET` request to retrieve information for a specific project by its ID:
  - `http://127.0.0.1:8000/api/projects/1/`

### PUT Requests

- **Making Changes to a Client**: After running the server, use the following URL with a `PUT` request:
  - `http://127.0.0.1:8000/api/clients/1`

- **Making Changes to a Project**: After running the server, use the following URL with a `PUT` request:
  - `http://127.0.0.1:8000/api/projects/1`

### DELETE Requests

- **Deleting a Client**: After running the server, use the following URL with a `DELETE` request:
  - `http://127.0.0.1:8000/api/clients/1`

- **Deleting a Project**: After running the server, use the following URL with a `DELETE` request:
  - `http://127.0.0.1:8000/api/projects/1`
