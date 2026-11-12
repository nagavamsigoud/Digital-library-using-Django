# Known limitations

These are intentionally disclosed rather than presented as completed features:

- The book-request workflow described in the academic report is not implemented in the code.
- The rating counters start at seeded values (one review, five stars), so a book with no reviews shows an average of 5.0 until the first review is recorded. Fixing this requires the aggregate-query migration in the roadmap.
- Online payment is not implemented. The checkout is a cash-on-delivery demonstration only.
- The delivery-region dropdowns contain the sample locations from the original project and must be adapted to the intended service area.
- Shipping is a fixed configurable fee, not a carrier or distance-based calculation.
- Review aggregates use legacy denormalized counters (`totalreview` and `totalrating`). A future migration should calculate averages from `Review` rows and remove counter drift risk.
- The cart is session-backed. It is not reserved inventory; stock is checked again during checkout.
- Row-level locking depends on database support. Use PostgreSQL for production concurrency testing; SQLite does not provide equivalent row-locking behavior.
- Media files remain in the repository as sample assets. Confirm licensing and move user-uploaded production media to object storage.
- Email verification, password reset UI, rate limiting, structured audit logs, and full end-to-end tests remain future work.
- No deployment, browser-level acceptance test, or live payment test has been performed.
