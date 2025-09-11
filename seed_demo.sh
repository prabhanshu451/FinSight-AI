#!/usr/bin/env bash
# Seed demo data into Django app inside the web container.
# Run after migrations are applied.

set -e

echo "Loading demo fixtures..."
docker compose exec web python manage.py loaddata django_project/fixtures/demo_users.json
docker compose exec web python manage.py loaddata django_project/fixtures/demo_expenses.json
docker compose exec web python manage.py loaddata django_project/fixtures/demo_forecasts.json
echo "Demo data loaded."
