# Database and migration notes

The source archive included a local SQLite database. It is intentionally excluded from this cleaned project because it contained user and order records. A fresh checkout should create its own database using:

```bash
python manage.py migrate
python manage.py createsuperuser
```

The new migrations update book/order money fields to decimal types, correct category/writer update timestamps, remove unsupported payment account/transaction fields, and protect books referenced by historical order items.

**Existing database warning:** applying the new order migration removes the old `account_no` and `transaction_id` columns. Back up any database you own before migrating. Do not carry real payment credentials into the new schema. For this public demo repository, start with a fresh local database and seed catalog records through Django Admin.
