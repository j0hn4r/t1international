from __future__ import unicode_literals

from django.db import models
from glitter.assets.fields import AssetForeignKey
from glitter.models import BaseBlock


class Billboard(BaseBlock):
    COLOUR_CHOICES = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('dark-green', 'Dark Green'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )

    background_colour = models.CharField(max_length=20, blank=True, choices=COLOUR_CHOICES)
    background_image = AssetForeignKey(
        'glitter_assets.Image', null=True, blank=True, related_name='+')
    image = AssetForeignKey('glitter_assets.Image', null=True, related_name='+')
    title = models.CharField(max_length=100)
    link = models.URLField()
    link_text = models.CharField(max_length=100, blank=True)
    new_window = models.BooleanField('Open link in new window', default=False)


class Poster(BaseBlock):
    background_image = AssetForeignKey('glitter_assets.Image', null=True, blank=True)
    content = models.TextField()


class Signees(BaseBlock):
    pass
