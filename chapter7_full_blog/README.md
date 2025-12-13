Chapter 7 - Full Django Blog (ready-to-run)

Features included:
- CRUD for posts (author-only edit/delete)
- User authentication: register, login, logout
- Comments (authenticated users)
- Pagination (5 posts/page)
- Search (by title/content)
- Categories (slug)
- Slug-based post URLs
- Like/unlike posts

Quick setup:
1. Unzip the folder.
2. Create & activate virtualenv:
   python -m venv .venv
   .venv\Scripts\activate   (Windows) or source .venv/bin/activate
3. Install Django:
   pip install django
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver
7. Visit http://127.0.0.1:8000/

Notes:
- Replace SECRET_KEY for production.
- This is intentionally minimal: enhance styling/templates as needed.
