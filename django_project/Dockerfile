FROM python:3.11-slim
WORKDIR /app

# Install system dependencies needed to build some scientific libraries and Prophet
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    git \
    curl \
    wget \
    python3-dev \
    default-libgomp \
    libatlas-base-dev \
    pkg-config \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Optional: to use cmdstan (recommended for Prophet), you can install cmdstan via cmdstanpy in runtime:
#   pip install cmdstanpy
#   python -c "import cmdstanpy; cmdstanpy.install_cmdstan()"
# Note: cmdstan download may take time and increase image size.

COPY requirements /app/requirements
RUN pip install --upgrade pip && pip install -r requirements/base.txt

COPY . /app
ENV PYTHONUNBUFFERED=1
