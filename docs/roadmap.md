# Roadmap

## Next engineering improvements
1. Add end-to-end tests for the complete browse-to-order journey.
2. Replace the legacy rating counters with an aggregate query over `Review` records and prevent duplicate reviews if desired.
3. Replace the fixed shipping fee with a location-aware delivery calculation and delivery-region configuration.
4. Add a real payment provider only if required, using provider-hosted/tokenized payment flows; never store raw card details.
5. Add email verification, password reset, rate limiting, and structured logging.
6. Move media to object storage and deploy with PostgreSQL, HTTPS, backups, and monitoring.
7. Add CI coverage, accessibility checks, and dependency/security scanning.
