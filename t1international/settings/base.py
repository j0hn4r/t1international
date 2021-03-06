# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Django settings for t1international project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Production / development switches
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')


# Email
# https://docs.djangoproject.com/en/1.8/ref/settings/#email

ADMINS = (
    ('Blanc Ltd', 'studio@blanc.ltd.uk'),
)

MANAGERS = ADMINS

SERVER_EMAIL = 't1international@blanctools.com'

DEFAULT_FROM_EMAIL = 't1international@blanctools.com'

EMAIL_SUBJECT_PREFIX = '[t1international] '


# Project root apps
PROJECT_APPS_ROOT = os.path.join(BASE_DIR, 'apps')
sys.path.append(PROJECT_APPS_ROOT)


DEFAULT_APPS = [
    # These apps should come first to load correctly.
    'blanc_admin_theme',
    'core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
]


THIRD_PARTY_APPS = [
    'adminsortable',
    'crispy_forms',
    'django_mptt_admin',
    'glitter',
    'glitter.assets',
    'glitter.blocks.banner',
    'glitter.blocks.call_to_action',
    'glitter.blocks.form',
    'glitter.blocks.html',
    'glitter.blocks.image',
    'glitter.blocks.redactor',
    'glitter.blocks.video',
    'glitter.pages',
    'glitter_news',
    'mptt',
    'paginationlinks',
    'raven.contrib.django.raven_compat',
    'sorl.thumbnail',
]


PROJECT_APPS = [
    'blocks',
    'donate',
    'pages',
    'footer',
    'signees',
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'glitter.pages.middleware.PageFallbackMiddleware',
    'glitter.middleware.ExceptionMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 't1international.urls'

WSGI_APPLICATION = 't1international.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}


# Caches
# https://docs.djangoproject.com/en/1.8/topics/cache/

CACHES = {}
if os.environ.get('MEMCACHED_SERVERS'):
    CACHES['default'] = {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': os.environ['MEMCACHED_SERVERS'].split(' '),
        'KEY_PREFIX': os.environ.get('MEMCACHED_PREFIX'),
    }
else:
    CACHES['default'] = {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs/static')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# File uploads
# https://docs.djangoproject.com/en/1.8/ref/settings/#file-uploads

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs/media')

DEFAULT_FILE_STORAGE = os.environ.get(
    'DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage'
)


# Templates
# https://docs.djangoproject.com/en/1.8/ref/settings/#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'footer.context_processors.links',
            ],
        },
    },
]


# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}


# Any other application config goes below here

# Sites framework
SITE_ID = 1

# Cloud storage
CONTENTFILES_PREFIX = 't1international'
CONTENTFILES_SSL = True

# Thumbnail generation
THUMBNAIL_PREFIX = 'thumbs/'
THUMBNAIL_PRESERVE_FORMAT = True
THUMBNAIL_QUALITY = 100

# Glitter
GLITTER_DEFAULT_BLOCKS = (
    ('glitter_redactor.Redactor', 'Text'),
    ('glitter_image.ImageBlock', 'Image'),
    ('glitter_html.HTML', 'HTML'),
)

# Forms
CRISPY_TEMPLATE_PACK = 'uni_form'

# Donations
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
DONATE_CURRENCY = 'USD'
DONATE_SYMBOL = '$'

# Webfaction SMTP
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
