# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from glitter.models import BaseBlock

from . import choices as pages_choices


class Blockquote(BaseBlock):
    quote = models.TextField()
    citation = models.CharField(max_length=256)
    background_color = models.CharField(
        choices=pages_choices.BLOCKQUOTE_COLOUR_CHOICES, max_length=16
    )


class FAQ(BaseBlock):
    question = models.TextField()
    answer = models.TextField()


class SignupFormBlock(BaseBlock):
    pass
