import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *



sentry_sdk.init(
    dsn=os.environ.get('SENTRY_ID'),
    integrations=[DjangoIntegration()]
)

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Staff <staff@yummy.com>'

ADMINS = (
    ('Admin', EMAIL_HOST_USER),
)
MANAGERS = ADMINS

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [
    'yum-miam.herokuapp.com',
]


DATABASES['default'] = dj_database_url.config()

DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'