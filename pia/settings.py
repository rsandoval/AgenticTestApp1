import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key")
DEBUG = os.environ.get("DEBUG", "1") in ("1", "true", "True")
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'training',
    'dashboard',
    'landing',
]

# Custom user model
AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pia.wsgi.application'
ASGI_APPLICATION = 'pia.asgi.application'

# Database configuration: prefer MSSQL Server with provided credentials by default.
# Fallback to SQLite for local development when explicitly requested.
USE_SQLITE_DEV = os.environ.get('PIAMENTOR_USE_SQLITE_DEV') == '1'
if not USE_SQLITE_DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': os.environ.get('PIAMENTOR_DB_NAME', 'DB_37113_piamentortst'),
            'USER': os.environ.get('PIAMENTOR_DB_USER', 'DB_37113_piamentortst_user'),
            'PASSWORD': os.environ.get('PIAMENTOR_DB_PASSWORD', '0192=PMentor'),
            'HOST': os.environ.get('PIAMENTOR_DB_HOST', 's31.winhost.com'),
            'PORT': os.environ.get('PIAMENTOR_DB_PORT', '1433'),
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
                'encrypt': 'true',
                'TrustServerCertificate': 'true',
            },
        }
    }
else:
    # Local development: use SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'assets']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL = '/'

DEBUG_PROPAGATE_EXCEPTIONS = True
