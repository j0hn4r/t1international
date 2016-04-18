"""
WSGI config for t1international project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import sys

# Python 2 threading problems
if sys.version_info < (3,):
    import _strptime  # noqa

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
