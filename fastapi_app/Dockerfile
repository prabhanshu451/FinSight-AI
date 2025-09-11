FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    curl \
    wget \
    python3-dev \
    default-libgomp \
    libatlas-base-dev \
    pkg-config \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements /app/requirements
RUN pip install --upgrade pip && pip install -r requirements/base.txt

COPY . /app
