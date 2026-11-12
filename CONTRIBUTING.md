# Contributing

1. Create a feature branch from the current default branch.
2. Create and activate a virtual environment; install `requirements.txt`.
3. Make focused changes and add or update tests.
4. Run `python manage.py check`, `python manage.py makemigrations --check --dry-run`, and `python manage.py test`.
5. Open a pull request describing the change, motivation, test evidence, and any migration or configuration impact.

Do not commit secrets, `.env` files, database dumps, personal data, or generated Python bytecode. For security issues, follow `SECURITY.md` rather than opening a public issue.
