import dj_database_url

from .settings.base import *

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Justin <muypicky@gmail.com>'

ADMINS = (
    ('Admin', EMAIL_HOST_USER),
)
MANAGERS = ADMINS

SECRET_KEY = os.environ.get('SECRET_KEY', 'j2b_z(*4w+#)t^nz3)0n3da(tcj&3##klo73m76(x7%3z)b%85n!')

ALLOWED_HOSTS = []


DATABASES['default'] = dj_database_url.config()

DEBUG = False
# TEMPLATE_DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'