import os
from .settings import *

# Override with environment variables for production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Allow hosts - default to all if not specified (Render requires this)
hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '*')
if hosts == '*':
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [h.strip() for h in hosts.split(',') if h.strip()]

# Security defaults
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'False') == 'True'
X_FRAME_OPTIONS = 'DENY'

# Use WhiteNoise for static file serving in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow additional trusted origins (comma-separated)
trusted = os.environ.get('CSRF_TRUSTED_ORIGINS', 'https://portfoilo1-api.onrender.com')
if trusted:
    CSRF_TRUSTED_ORIGINS = [t.strip() for t in trusted.split(',') if t.strip()]

# CORS for frontend (allow localhost for dev, add production URLs as needed)
CORS_ALLOWED_ORIGINS_FROM_ENV = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173')
if CORS_ALLOWED_ORIGINS_FROM_ENV:
    CORS_ALLOWED_ORIGINS = [origin.strip() for origin in CORS_ALLOWED_ORIGINS_FROM_ENV.split(',') if origin.strip()]

# Database from DATABASE_URL (Render managed Postgres or other URL)
try:
    import dj_database_url
except Exception:
    dj_database_url = None

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL and dj_database_url:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=not DEBUG)
    }
