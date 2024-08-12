# UPC_API

## Overview

This project is a Django REST Framework-based API for managing users, clients, and projects. The API allows for the registration of clients, fetching client information, editing/deleting client information, adding new projects for a client, assigning users to those projects, and retrieving projects assigned to logged-in users.

## Features

- **User Management**: Uses Django's default admin template to create/register users.
- **Client Management**: Create, retrieve, update, and delete client information.
- **Project Management**: Add new projects, assign users to projects, and retrieve projects assigned to logged-in users.

## Technical Requirements

- **Framework**: Django REST Framework (install using `pip install djangorestframework`)
- **Database**: MySQL

## Creating Superuser

To create a superuser, follow these steps:

```bash
python manage.py shell
