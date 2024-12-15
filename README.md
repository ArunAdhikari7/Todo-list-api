# Django To-Do API

This project is a **RESTful API** built with Django and Django REST Framework for managing a simple to-do list application. The API allows users to perform CRUD operations on tasks, including creating, retrieving, updating, and deleting tasks.

Features

Create Tasks: Add a new task with a title, description, and status.
Retrieve Tasks: Fetch all tasks or a specific task by its ID.
Update Tasks: Modify the status of a task (pending, in-progress, completed).
Delete Tasks: Remove a task from the list.

Technologies Used

Framework:	Django 4.x, Django REST Framework
Database:	SQLite 
Tools: 		Git for version control
Language: 	Python 3.x

API Endpoints

**Base URL:** `http://127.0.0.1:8000/api/tasks/`

 HTTP Method | Endpoint                      | Description                       |
-------------|-------------------------------|-----------------------------------|
 POST        | `/`                           | Create a new task                |
 GET         | `/all/`                       | Retrieve all tasks               |
 GET         | `/<id>/`                      | Retrieve a task by ID            |
 PUT         | `/update/<id>/`               | Update the status of a task      |
 DELETE      | `/delete/<id>/`               | Delete a task by ID              |

Task Model
title: (string) The title of the task.
description: (string) A brief description of the task.
status: (string) The task's status (default: `"pending"`). Options: `"pending"`, `"in-progress"`, `"completed"`.

Prerequisites
Python 3.8+
Pip
Virtualenv (optional)

Setup Instructions

1. Clone Repository
git clone https://github.com/your-username/django-todo-api.git
cd django-todo-api

2. Create a Virtual Environment
python -m venv env
source env/bin/activate  #env\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up the Database
python manage.py makemigrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver

Testing the API
You can test the API endpoints using:

Postman or cURL
Browser-based tools like Django REST Framework's built-in interface (navigate to the endpoints in your browser).
Example cURL Commands:


