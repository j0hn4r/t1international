# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import Link

admin.site.register(Link, SortableAdmin)
