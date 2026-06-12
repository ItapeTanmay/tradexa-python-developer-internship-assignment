# Tradexa Python Developer Internship Assignment

## Submitted by: Tanmay Itape

---

## Project Overview

A Django 6.x application with two separate apps (`users` and `products`) and two independent SQLite databases. Demonstrates multi-database routing, custom user authentication, ORM relationships with `db_constraint=False`, and admin customization.

---

## Features

- Custom user model (`AbstractUser`)
- User authentication (login/logout) using Django's built-in views
- Post creation (only for authenticated users) with `@login_required`
- `ForeignKey` with `db_constraint=False` — ORM relationship without a database-level constraint
- Separate databases for `users` and `products` apps
- Database router for read/write/migration routing
- Admin interface for all models
- Public product listing page

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Django 6.x |
| Frontend | Bootstrap 5 (CDN) |
| Databases | SQLite (two separate databases) |
| Config | python-decouple (environment variables) |

---

## Folder Structure

```
tradexa_assignment/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── routers.py
│   └── wsgi.py
├── users/
│   ├── models.py               # User, Post
│   ├── views.py                # home, create_post
│   ├── forms.py                # PostForm
│   ├── admin.py
│   └── templates/users/
│       ├── home.html
│       ├── login.html
│       └── create_post.html
├── products/
│   ├── models.py               # Product
│   ├── views.py                # product_list
│   ├── admin.py
│   └── templates/products/
│       └── product_list.html
├── users_db.sqlite3
├── products_db.sqlite3
├── manage.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone (https://github.com/ItapeTanmay/tradexa-python-developer-internship-assignment.git)
cd tradexa_assignment
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Open .env and set your SECRET_KEY
```

### 5. Run migrations for both databases

```bash
python manage.py makemigrations users products
python manage.py migrate --database=default
python manage.py migrate --database=products_db
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Access the application

| Page | URL |
|---|---|
| Home | `http://127.0.0.1:8000/` |
| Login | `http://127.0.0.1:8000/login/` |
| Create Post | `http://127.0.0.1:8000/create/` |
| Products | `http://127.0.0.1:8000/products/` |
| Admin | `http://127.0.0.1:8000/admin/` |

---

## Database Routing

The project uses a custom router (`config/routers.py`) to keep the two apps isolated:

| App | Database | File |
|---|---|---|
| `users` | `default` | `users_db.sqlite3` |
| `products` | `products_db` | `products_db.sqlite3` |
| `auth`, `admin`, `sessions` | `default` | `users_db.sqlite3` |

### Router Methods

| Method | Purpose |
|---|---|
| `db_for_read()` / `db_for_write()` | Directs reads and writes based on `app_label` |
| `allow_relation()` | Prevents relations across databases |
| `allow_migrate()` | Ensures migrations run only on the correct database |

---

## Testing

The following scenarios were manually tested:

- **Authentication** — login/logout flow, `@login_required` redirect for unauthenticated users
- **Admin CRUD** — create, read, update, delete for User, Post, and Product models
- **Database isolation** — verified each app's tables exist only in the correct `.sqlite3` file
- **Edge cases** — empty form submissions, unauthorized access attempts, cross-DB isolation

---

## Screenshots

*(See the attached PDF report for all screenshots)*

---

## Future Improvements

- User registration flow
- Edit and delete posts
- Product CRUD for authenticated users
- REST API using Django REST Framework
- PostgreSQL support for production deployments

---

## License

This project is submitted as part of the Tradexa Python Developer Internship assignment and is intended for evaluation purposes only.
