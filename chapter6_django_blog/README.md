# Django Blog - Chapter 6 (Minimal Project)

What's included:
- A minimal Django project named `django_project`
- An app `blog` with `Post` model, admin registration, views, urls, and templates.
- Simple templates: list (home) and detail pages.

Quick setup:
1. Unzip the folder.
2. Create a virtualenv and install Django:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # windows
   # or: source .venv/bin/activate  # mac / linux
   pip install django
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create superuser and run server:
   ```
   python manage.py createsuperuser
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/ and admin at /admin to add posts.

Notes:
- This is a minimal project for learning Chapter 6 concepts (models, views, templates, urls).
- SECRET_KEY in settings.py should be replaced for production.
