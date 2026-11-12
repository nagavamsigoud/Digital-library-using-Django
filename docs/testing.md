# Testing status

Automated Django tests cover core cart operations, authenticated review submission and rating validation, and order ownership/privacy.

## Last recorded run

- Command: `python manage.py test`
- Result: 9 tests, OK
- Also passing: `python manage.py check` (no issues) and `python manage.py makemigrations --check --dry-run` (no changes)
- Environment: Python 3.12.3, Django 5.2.19, SQLite, installed from `requirements.txt`

Re-run these three commands in your own environment and update this section before claiming the project is verified there.

## Not yet covered

This test suite is not exhaustive. Additional coverage should include registration/login, search behavior, cart endpoints/CSRF, stock races under PostgreSQL, checkout rollback, invoice rendering, pagination, and admin permissions.
