# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from adminsortable.models import SortableMixin


@python_2_unicode_compatible
class Link(SortableMixin):
    title = models.CharField(max_length=100, db_index=True)
    link = models.URLField()
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.title
