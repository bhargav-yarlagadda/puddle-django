# Django Recipe App

This Django Recipe application allows users to create, update, delete, and view recipes. The app also includes user authentication, enabling users to register, log in, and log out securely.

## Features

- **CRUD Operations for Recipes**:
  - Create new recipes by adding a name, description, and image.
  - View all existing recipes.
  - Update existing recipes with new information or images.
  - Delete unwanted recipes.

- **User Authentication**:
  - User registration to create a new account.
  - Secure login and logout functionality.
  - Error messages for invalid credentials or duplicate usernames.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bhargav-yarlagadda/puddle-django
   cd puddle


2. **migrations**  
    ```bash
    python manage.py migrate


3. **start the application**
    ```bash
    python manage.py runserver


4. **application structure**

    ```bash
        puddle/                  # Root directory of your Django project
        │
        ├── asgi.py              # ASGI config for async support (used in deployment)
        ├── settings.py          # Main settings/configuration for the Django project
        ├── urls.py              # Main URL routing for the entire project
        ├── wsgi.py              # WSGI config for deployment
        └── __init__.py          # Indicates that this is a Python package

        puddleApplication/       # Application directory within the Django project
        │
        ├── migrations/          # Database migration files (auto-generated)
        ├── static/              # Static files like CSS, JS, and images
        ├── templates/           # HTML templates for rendering views
        │   ├── recipes.html     # Template for displaying all recipes
        │   └── update.html      # Template for updating a recipe
        ├── models.py            # Database models (e.g., Recipe model)
        ├── views.py             # Views for handling logic (CRUD, authentication)
        ├── admin.py             # Configuration for Django Admin interface
        ├── urls.py              # URL routing specific to this app
        └── __init__.py          # Indicates that this is a Python package
