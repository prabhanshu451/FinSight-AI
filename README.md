# FinSight-AI

FinSight-AI is a full-stack scaffold for building financial dashboards and forecasting applications.  
It combines **Django** + **FastAPI** microservices, **Celery**, **Redis**, and **PostgreSQL** with a modern frontend to deliver real-time insights and predictive analytics.

---

## 📘 Features

- 📊 Financial time series forecasting with **Prophet** (with fallback strategy)  
- ⚡ Real-time updates using **WebSockets (Django Channels)**  
- 🛠️ Background job scheduling with **Celery + Redis**  
- 🗄️ Relational data with **PostgreSQL**  
- 🎨 Dashboard UI with **TailwindCSS + Bootstrap**, including dark mode and toast notifications  
- 🐳 Dockerized setup for easy local development & deployment  

---

## 📂 Project Structure

| Folder / File             | Purpose |
|----------------------------|---------|
| `django_project/`         | Django backend (models, views, WebSocket logic) |
| `fastapi_app/`            | FastAPI microservice for forecasting |
| `docs/`                   | Documentation, deployment notes |
| `demo_data/`              | Sample / seed data |
| `docker-compose.yml`      | Defines containers (web, api, db, redis, worker) |
| `seed_demo.sh`            | Script to populate demo data |
| `.env.example`            | Example environment variables |
| `requirements/`           | Python dependencies |

---

## ⚙️ Getting Started

### 1️⃣ Prerequisites
- Git  
- Docker & Docker Compose installed  
- (Optional) Python 3.9+ for running locally without Docker  

### 2️⃣ Clone the Repo
```bash
git clone https://github.com/prabhanshu451/FinSight-AI.git
cd FinSight-AI

3️⃣ Configure Environment

Copy the example environment file:

cp .env.example .env


Fill in your DB credentials, secret keys, and other variables.

4️⃣ Start Services (Docker Compose)
docker-compose up --build


This will start:

Django web app

FastAPI forecasting service

PostgreSQL

Redis

Celery worker & beat

5️⃣ Run Migrations & Seed Demo Data
docker-compose exec web python manage.py migrate
docker-compose exec web sh /app/seed_demo.sh

6️⃣ Access the App

Django web app → http://localhost:8000

Django admin → http://localhost:8000/admin

FastAPI service → http://localhost:8001
