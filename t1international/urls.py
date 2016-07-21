# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from glitter import block_admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blockadmin/', include(block_admin.site.urls)),

    # Donations
    url(r'^donate/', include('donate.urls', namespace='donate')),

    # News
    url(r'^blog/', include('glitter_news.urls', namespace='glitter-news')),
]

# Make it easier to see a 404 page under debug
if settings.DEBUG:
    from django.views.defaults import page_not_found

    urlpatterns += [
        url(r'^404/$', page_not_found),
    ]

# Serving static/media under debug
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
