# Django Blog Project

> **Note**: This is a practice project created to learn more about Django framework and its features. It is currently a work in progress (WIP) and is being used as a learning exercise.

A blog platform built with Django that allows users to create and publish articles, add comments, and organize content by categories.

## Security Note

This repository contains example code. For production use:
1. Never commit `.env` files or `settings.py` with sensitive data
2. Keep `SECRET_KEY` and other credentials secure
3. Use environment variables for sensitive settings
4. Review Django's deployment checklist before going live

## Features

- Article creation and management
- Category-based organization
- Search functionality
- Responsive design with Bootstrap
- Image upload support
- Admin interface for content management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd django_project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On Unix or MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your web browser.

## Usage

1. Access the admin interface at http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Create categories in the admin interface
4. Create articles and manage comments
5. Visit the main blog page to view published articles

## Project Structure

- `blog/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL patterns
  - `templates/` - HTML templates
- `blog_project/` - Project settings
- `media/` - User-uploaded files
- `static/` - Static files (CSS, JavaScript, images)