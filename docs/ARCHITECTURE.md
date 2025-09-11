# FinSightAI Architecture (v2)

- Django + Channels (ASGI via Daphne) serves frontend, admin, and WebSockets.
- FastAPI hosts forecasting microservice (Prophet optional).
- Celery + Redis for background jobs. Flower for monitoring.
- Postgres stores data.
