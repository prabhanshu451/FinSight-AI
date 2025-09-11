# Deployment Notes

1. Copy .env.example to .env and set secrets.
2. Build: docker compose build
3. Run: docker compose up --build
4. Create migrations and superuser via docker exec or run commands.
Note: Prophet has system dependencies — if you plan to run Prophet in production, install its system requirements (PyStan / cmdstan) per Prophet docs.
