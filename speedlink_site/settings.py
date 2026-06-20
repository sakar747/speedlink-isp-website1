import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-before-submission-demo')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mongodb_backend',
    'complaints',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'speedlink_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'speedlink_site.wsgi.application'
ASGI_APPLICATION = 'speedlink_site.asgi.application'

# MongoDB connection using the Official Django MongoDB Backend.
# For local MongoDB, keep MONGODB_URI=mongodb://localhost:27017
# For MongoDB Atlas, set MONGODB_URI to your Atlas connection string.
DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_backend',
        'HOST': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017'),
        'NAME': os.environ.get('MONGODB_NAME', 'speedlink_isp_db'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.environ.get('DJANGO_TIME_ZONE', 'Asia/Kathmandu')
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django_mongodb_backend.fields.ObjectIdAutoField'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STAFF_USERNAME = os.environ.get('STAFF_USERNAME', 'admin')
STAFF_PASSWORD = os.environ.get('STAFF_PASSWORD', 'admin123')
