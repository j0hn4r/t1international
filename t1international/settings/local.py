# -*- coding: utf-8 -*-

from importlib import import_module
import os

from .base import *  # NOQA @UnusedWildImport


DEBUG = True

# Enable debugging for templates
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
            ],
            'debug': True,
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 't1international_django'),
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
    },
}

INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]


# Add flat theme if module is installed.
try:
    import_module('flat')
except ImportError:
    pass
else:
    INSTALLED_APPS.insert(0, 'flat')


MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE_CLASSES


COVERAGE_EXCLUDES_FOLDERS = ['/var/envs/t1international/lib/python2']


SECRET_KEY = 't1international'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
