
from noonpost.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv("SECRET_KEY_DEV"))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.getenv("DEBUG"))

ALLOWED_HOSTS = [str(os.getenv("ALLOWED_HOSTS_DEV"))]


SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

DEFAULT_FROM_EMAIL = "dev"
SERVER_EMAIL = "noonpost"


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True