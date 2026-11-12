# Architecture

The application is a server-rendered Django monolith. The root `bookstore` package configures Django and routes requests to four feature apps.

- `store`: catalog entities, registration/login/logout, book pages, and reviews.
- `search`: query-string search across book title, category name, and writer name.
- `cart`: a session-backed cart; cart contents are not stored as database rows.
- `order`: checkout, persisted orders/order items, order history, and PDF invoice rendering.

Django templates render HTML. Static CSS/JavaScript assets provide presentation and browser interactions. SQLite is the default local database; PostgreSQL can be configured with `DATABASE_URL`.

## Request flow

1. Browser sends a request to Django's root URL router.
2. The relevant app view validates the request and accesses models or the session.
3. Django ORM reads/writes the database.
4. The view renders a template or returns a redirect/JSON/PDF response.

## Checkout flow

Checkout requires authentication and a non-empty cart. The order and order-item rows are created inside `transaction.atomic()`. Stock is checked and decremented before commit. The cart is cleared only after a successful transaction. Payment is not processed; the demo payment method is cash on delivery.
