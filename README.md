# Online Bookstore Management System

A Django-based bookstore web application for browsing books, searching by title/category/author, registering and signing in, managing a session-based cart, placing cash-on-delivery demo orders, reviewing books, and downloading an order invoice as a PDF.

> **Project scope:** This is an academic/demo bookstore application. It does not integrate a payment provider, process card payments, or verify online transactions. Checkout is configured for cash on delivery. Do not enter or store real payment credentials.

## Features

- Browse recently added books, categories, authors, and book details.
- Search books by title, category, or author.
- Register and authenticate users using Django authentication.
- Add, update, and remove items in a session-backed cart.
- Submit 1–5 star book reviews when signed in.
- Create orders and order items in a database transaction.
- Reduce available stock when an order is created.
- View only the signed-in user's orders and download their invoices.
- Manage catalog data through Django Admin.

## Technology

- Python 3.10+
- Django 5.2 LTS
- SQLite for local development; PostgreSQL can be configured with `DATABASE_URL`
- Django templates, HTML, CSS, JavaScript, Bootstrap assets
- django-crispy-forms with crispy-bootstrap4
- xhtml2pdf for invoice generation

## Quick start

### 1. Clone and enter the project

```bash
git clone https://github.com/nagavamsigoud/Digital-library-using-Django.git
cd Digital-library-using-Django
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies and configure environment

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, generate a new secret key, and set `DJANGO_SECRET_KEY`. Django does not automatically load `.env` files in this setup; export the variables in your shell or use your deployment platform's environment-variable settings. For local PowerShell, for example:

```powershell
$env:DJANGO_SECRET_KEY = "your-generated-secret"
$env:DJANGO_DEBUG = "True"
```

### 4. Apply migrations and create an admin user

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ and visit `/admin/` to manage books, categories, writers, and orders.

See `docs/architecture.md` for the application structure, `docs/decision-log.md` for key engineering decisions, `docs/known-limitations.md` for unfinished production work, and `docs/database-migrations.md` before migrating an existing database.

## Tests and quality checks

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```

The tests cover selected cart, review, and order-privacy behaviors. They are a starting point, not a claim of exhaustive coverage.

## Configuration

| Variable | Purpose | Local default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django signing secret | Development-only fallback; replace it |
| `DJANGO_DEBUG` | Debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `TIME_ZONE` | Application timezone | `UTC` |
| `SHIPPING_FEE` | Fixed checkout shipping amount | `100.00` |
| `DATABASE_URL` | Optional PostgreSQL URL | SQLite is used when unset |

Set `DJANGO_DEBUG=False`, a unique secret, and production hosts before deployment. HTTPS settings are enabled when debug is off.

## Project structure

```text
bookstore/     Django settings, root URLs, WSGI entry point
store/         Catalog, users, book reviews, templates and static assets
cart/          Session-based shopping cart
search/        Catalog search
order/         Checkout, order history, and PDF invoices
docs/          Architecture, data model, workflows, and operations notes
files/         Project-provided book and author images (media assets)
```
## screen shots

<img width="1764" height="864" alt="Screenshot 2026-04-19 152639" src="https://github.com/user-attachments/assets/a1573cdb-78b5-4420-b3c6-ff805c89ebca" />

<img width="1751" height="825" alt="Screenshot 2026-04-19 152742" src="https://github.com/user-attachments/assets/207c67c0-9c3b-4d24-a77b-b7214ac5a637" />

<img width="1647" height="780" alt="Screenshot 2026-04-19 152811" src="https://github.com/user-attachments/assets/ff7224db-09dc-452e-8c5d-b12a4e047fce" />

<img width="1646" height="872" alt="Screenshot 2026-04-19 152834" src="https://github.com/user-attachments/assets/4f069760-8776-417c-b9c1-f12cc7c8890a" />

<img width="1629" height="557" alt="Screenshot 2026-04-19 152856" src="https://github.com/user-attachments/assets/6564f742-cfd3-4251-9bbf-b49143f93c81" />

<img width="1642" height="778" alt="Screenshot 2026-04-19 152923" src="https://github.com/user-attachments/assets/c3b145b5-3cbe-4b32-b81f-052eaf36bb3d" />

<img width="1237" height="670" alt="Screenshot 2026-04-19 152950" src="https://github.com/user-attachments/assets/a678b8e9-c248-4fea-b8d9-bded3bee6136" />

<img width="1232" height="588" alt="Screenshot 2026-04-19 153009" src="https://github.com/user-attachments/assets/0495b838-daec-4d02-91dd-a53e040efa94" />

<img width="1237" height="671" alt="Screenshot 2026-04-19 153038" src="https://github.com/user-attachments/assets/a92fc7d5-27ba-4db4-8071-be79241a9f7f" />



## Important limitations

- There is no payment gateway integration. Orders use cash on delivery in this demo.
- Shipping is a configurable fixed amount (`SHIPPING_FEE`, default `100.00`) used by both checkout and the summary.
- The delivery-region choices are sample values inherited from the academic project and should be replaced for the intended market.
- Uploaded media is stored locally. Production deployments should use durable object storage and a production-grade media-serving strategy.
- SQLite is suitable for local development; use PostgreSQL for a multi-user deployment.
- No production deployment has been performed as part of this cleanup.

## Security notes

- Never commit `.env`, database files, real user data, or production secrets.
- If the old hard-coded secret or SQLite database was previously pushed to a public Git repository, rotate the secret and remove sensitive history using a carefully reviewed history rewrite. Deleting the file in a new commit does not erase earlier Git history.
- Review image/media licensing before publishing assets.
- Configure HTTPS, backups, logging, monitoring, and secure database credentials before deployment.

## License

No license has been added because the ownership and redistribution rights for the original project and bundled media have not been established. Add a license only after confirming you have the right to do so.

## Academic submission and later improvements

The original academic report is kept separate and unchanged. The GitHub repository contains later portfolio maintenance and improvements. 
