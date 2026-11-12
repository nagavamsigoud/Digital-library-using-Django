# Data model

## Catalog (`store`)

- `Category`: category name, slug, icon, and timestamps.
- `Writer`: author name, slug, biography, picture, and timestamps.
- `Book`: writer/category relationships, title, slug, decimal price, stock, cover/interior images, description, timestamps, and legacy rating counters.
- `Review`: customer, book, 1–5 rating, text, and creation timestamp.
- `Slider`: homepage slide title, image, and timestamps.

## Orders (`order`)

- `Order`: customer, shipping/contact fields, demo payment method, payable total, item count, timestamps, and paid flag.
- `OrderItem`: order, book, unit price snapshot, and quantity.

A review belongs to one user and one book. An order belongs to one customer and contains one or more order items. Order-item prices are stored as snapshots so a later catalog price change does not rewrite an existing order's item price.

## Cart

The cart is stored in the Django session as book IDs with quantities and price snapshots. It is not a relational database model.
