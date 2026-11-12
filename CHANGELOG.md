# Changelog

## Unreleased
- Fix cart clear so the in-memory cart is empty immediately after checkout.
- Guard missing book cover and interior images on the book page so books without files do not raise server errors.
- Remove committed local database and Python bytecode from the distributable source tree.
- Move Django secrets and host configuration to environment variables.
- Add CSRF-protected POST methods for cart changes and logout.
- Correct review persistence and rating validation.
- Restrict order history, details, and invoice access to the owning user.
- Make checkout transactional, validate stock, and snapshot current item prices.
- Remove unsupported card/bank credential fields; clarify cash-on-delivery demo behavior.
- Add project documentation, tests, dependency manifest, and GitHub Actions CI.
