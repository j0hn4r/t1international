# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Link


def links(request):
    return {
        'footer_links': Link.objects.all(),
    }
