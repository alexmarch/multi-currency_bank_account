## Run / Build
```bash
docker-compose up # Run and build application
docker-compose build # Build application
```
---
## Migrations
```bash
docker-compose run --rm webapp python mcurrency_bank_account/manage.py db migrate # detect migrations
docker-compose run --rm webapp python mcurrency_bank_account/manage.py db upgrade # apply migrations to db
```
---
## Tests
```bash
```