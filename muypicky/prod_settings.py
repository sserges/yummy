import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *



sentry_sdk.init(
    dsn="https://b9cc47781fac4828919a853b89c07e25@sentry.io/1291309",
    integrations=[DjangoIntegration()]
)

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Serge <agounkeserge@gmail.com>'

ADMINS = (
    ('Admin', EMAIL_HOST_USER),
)
MANAGERS = ADMINS

SECRET_KEY = os.environ.get('SECRET_KEY', 'j2b_z(*4w+#)t^nz3)0n3da(tcj&3##klo73m76(x7%3z)b%85n!')

ALLOWED_HOSTS = [
    'muypicky.herokuapp.com',
]


DATABASES['default'] = dj_database_url.config()

DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'