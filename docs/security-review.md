# Security review and operational checklist

The original source contained a hard-coded Django secret and `DEBUG=True`, and the supplied archive contained a SQLite database with user/order records. The cleaned repository removes the database and reads secrets/host settings from environment variables.

Implemented in this cleanup:
- CSRF-protected POST requests for cart mutations and logout.
- Authentication required for checkout and order history.
- Order detail and invoice queries are scoped to the authenticated owner.
- Review submissions require authentication and validate rating range.
- Checkout writes order/order-item records atomically and checks stock.
- Payment account/transaction fields are removed; this app does not collect card/bank credentials.

Before production:
- Set a unique secret, `DEBUG=False`, and exact allowed hosts.
- Use HTTPS and secure cookies; configure trusted proxy/CSRF origins for the hosting platform.
- Use PostgreSQL, durable media storage, backups, and monitoring.
- Review authorization in Django Admin and any future staff workflows.
- Add rate limiting, email verification/password reset, audit logging, and a privacy/data-retention policy.
- If secrets or private data were ever committed, rotate credentials and rewrite Git history; a normal delete commit is insufficient.
