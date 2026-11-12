# Engineering decision log

This log records implementation and repository-maintenance decisions for the portfolio version. It is not a record of decisions made during the original academic submission.

| ID | Decision | Rationale | Trade-off / limitation |
|---|---|---|---|
| D-01 | Keep the application as a Django server-rendered monolith. | The existing project is organized around Django apps, templates, and the ORM; a rewrite would add unnecessary scope. | Frontend and backend are not independently deployed services. |
| D-02 | Use environment variables for deployment-sensitive settings. | Secrets, debug mode, and allowed hosts should not be hard-coded in source control. | Developers must configure the environment before running outside the documented local defaults. |
| D-03 | Exclude local SQLite databases from the public repository. | The supplied database contained user and order records. | A fresh checkout must create its own database with migrations and add catalog data. |
| D-04 | Retain SQLite as the local-development default. | It keeps setup simple for an educational project. | PostgreSQL is recommended for production and concurrency validation. |
| D-05 | Keep the cart in the Django session. | This preserves the original lightweight cart design. | Cart contents are not shared across devices and do not reserve stock. |
| D-06 | Use POST requests with CSRF protection for cart mutations and logout. | State-changing operations should not be triggered by ordinary links or GET requests. | Clients must submit valid CSRF tokens. |
| D-07 | Scope order history, detail, and invoice access to the authenticated owner. | Order and invoice data are private to the customer who placed the order. | Staff access requires a separate, explicitly designed authorization path. |
| D-08 | Create an order and its items inside a database transaction. | A failed checkout should not leave a partially created order. | Concurrency behavior must be validated on the production database engine. |
| D-09 | Recheck and decrement stock during checkout. | Cart quantities can become stale between adding an item and placing an order. | SQLite does not provide the same row-locking guarantees as PostgreSQL. |
| D-10 | Store order-item prices as snapshots. | Historical orders should retain the price charged at the time of purchase. | Catalog price changes do not update historical order-item prices. |
| D-11 | Represent payment as a cash-on-delivery demo flow. | No payment-provider integration is present, so collecting card or bank credentials would be misleading and unsafe. | Online payment processing is outside the current scope. |
| D-12 | Keep automated tests and CI as an evolving baseline, not proof of exhaustive quality. | Automated checks help catch regressions in core behavior. | Additional end-to-end, concurrency, and deployment tests remain necessary. |

