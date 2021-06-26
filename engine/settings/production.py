from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

SENTRY_RELEASE = "production"
SENTRY_DSN = env('SENTRY_DSN')

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration(), ModulesIntegration()],
    release=VERSION,
    environment=SENTRY_RELEASE,

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
