# Django Blog Project

This is a simple blog application built using Django. Using authentication forms you can posting, tagging, searching, sharing, and commenting on blog posts, also you have a dashboard for your posts statistics.

## Features

- Display a list of blog posts with pagination
- Tagging of blog posts
- Search functionality for posts based on their title
- Share posts via email
- Add comments to blog posts

## Setup and Installation

To get started with this project, follow the steps below:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/django-blog-project.git
cd django-blog-project
```
### 2. Create a virtual environment

It is recommended to create a virtual environment to install the dependencies. You can do so with the following commands:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

Use `pip` to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

Run the following command to apply migrations and set up your database:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 5. Create a superuser

To access the Django admin and manage the blog, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the development server

Start the local development server:

```bash
python manage.py runserver
```
You can now visit `http://127.0.0.1:8000/account/login/` to view the blog.

Search Functionality

You can search for blog posts by title using the search bar on the main page. The search functionality uses Django's `TrigramSimilarity` to find relevant posts based on the similarity of the search query to post titles. The search results are displayed in order of relevance.

You can now visit `http://127.0.0.1:8000/blog/` to view the blog.

### 7. Project tree:

```bash
├── account
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── authentication.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── signals.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── authentication.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── signals.py
│   ├── templates
│   │   ├── account
│   │   │   ├── dashboard.html
│   │   │   ├── edit.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── register_done.html
│   │   │   └── user
│   │   │       ├── detail.html
│   │   │       └── list.html
│   │   └── registration
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── password_change_done.html
│   │       ├── password_change_form.html
│   │       ├── password_reset_complete.html
│   │       ├── password_reset_confirm.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_email.html
│   │       └── password_reset_form.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── sitemaps.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── sitemaps.py
│   ├── static
│   │   └── css
│   │       └── blog.css
│   ├── templates
│   │   ├── blog
│   │   │   ├── base.html
│   │   │   └── post
│   │   │       ├── comment.html
│   │   │       ├── details.html
│   │   │       ├── includes
│   │   │       │   └── comment_form.html
│   │   │       ├── latest_posts.html
│   │   │       ├── list.html
│   │   │       ├── post_create.html
│   │   │       ├── search.html
│   │   │       └── share.html
│   │   └── pagination.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── blog_tags.cpython-310.pyc
│   │   └── blog_tags.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   └── profile_pictures
│       ├── medium-742354810.jpg
│       ├── medium-742354810.jpg.180x180_q85.jpg
│       ├── straidframe.jpg
│       └── straidframe.jpg.180x180_q85.jpg
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── mysite_data.json
```

### If you have any troubles regarding installation or any other issues, so do not hesitate and contact me by mail: reneduchamp101@gmail.com. I will answer to you asap with great pleasure.
