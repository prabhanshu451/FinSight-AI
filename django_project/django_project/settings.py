import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
DEBUG = os.getenv('DEBUG', '1') == '1'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework','channels','core','expenses','forecasts','users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'django_project.urls'
TEMPLATES = [
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[BASE_DIR / 'templates'],
        'APP_DIRS':True,
        'OPTIONS':{'context_processors':[
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    }
]
WSGI_APPLICATION = 'django_project.wsgi.application'

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB','finsight'),
        'USER': os.getenv('POSTGRES_USER','finsight'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD','example'),
        'HOST': os.getenv('DB_HOST','db'),
        'PORT': os.getenv('DB_PORT',5432),
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
STATIC_URL='/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery
CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://redis:6379/0')

# Channels (WebSocket) configuration
ASGI_APPLICATION = 'django_project.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.getenv('REDIS_URL', 'redis://redis:6379/0')],
        },
    },
}

# WebSocket token expiry (configurable via admin)
WEBSOCKET_TOKEN_EXPIRY_SECONDS = int(os.getenv('WEBSOCKET_TOKEN_EXPIRY_SECONDS','3600'))
