
from noonpost.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [str(os.getenv("ALLOWED_HOSTS_PROD_1")), str(os.getenv("ALLOWED_HOSTS_PROD_2"))]


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

DEFAULT_FROM_EMAIL = "contact"
SERVER_EMAIL = "noonpost"
