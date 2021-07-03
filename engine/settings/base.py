"""
Django settings for engine project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from urllib.parse import urlparse

from django.conf import settings

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.modules import ModulesIntegration
import environ

from engine import VERSION

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env(
    ENABLE_EXPERIMENTAL_BLOG_COMMENTING=(bool, False),
    WAGTAIL_ENABLE_UPDATE_CHECK=(bool, False),
    SECURE_SSL_REDIRECT=(bool,True),
    COMPRESS_ENABLED=(bool, True),
    ALLOWED_HOSTS=(list, [])
)
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',
    'dashboard',
    'blocks',
    'flex',
    'blog',

    'wagtailmenus',
    'compressor',
    'wagtail_color_panel',
    'widget_tweaks',
    'django_comments_xtd',
    'django_comments',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings', 
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    "django.contrib.sitemaps",

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'wagtail.contrib.modeladmin',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'engine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'engine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_ENABLED = env('COMPRESS_ENABLED')
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_OFFLINE = False
LIBSASS_OUTPUT_STYLE = 'compressed'
LIBSASS_SOURCEMAPS = True
LIBSASS_PRECISION = 6

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail settings

WAGTAIL_SITE_NAME = "engine"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = env('BASE_URL')

# This is added to prevent "auto-created primary key" warnings with wagtailmenus
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Disable Wagtail Update Checking
WAGTAIL_ENABLE_UPDATE_CHECK = env('WAGTAIL_ENABLE_UPDATE_CHECK')

# Prevent users from editing pages that they have locked.
WAGTAILADMIN_GLOBAL_PAGE_EDIT_LOCK = True

WAGTAILMENUS_FLAT_MENUS_HANDLE_CHOICES = (
    ('footer', 'Footer'),
)

WAGTAILMENUS_ACTIVE_ANCESTOR_CLASS = "ancestor active"

SITE_ID = 1

ENABLE_EXPERIMENTAL_BLOG_COMMENTING = env('ENABLE_EXPERIMENTAL_BLOG_COMMENTING')

if ENABLE_EXPERIMENTAL_BLOG_COMMENTING:
    COMMENTS_APP = 'django_comments_xtd'
    COMMENTS_XTD_MODEL = 'blog.models.BlogPostComment'
    COMMENTS_XTD_MAX_THREAD_LEVEL = 16
    COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                        b"Aequam memento rebus in arduis servare mentem.")
    # COMMENTS_XTD_FROM_EMAIL = "engine-noreply@" + str(urlparse(BASE_URL).netloc)
    COMMENTS_XTD_FROM_EMAIL = "wm-engine@email.com"

DISK_MOUNT_POINT = env('METRICS_DISK_MOUNT_POINT')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('EMAIL_FROM_USER')

