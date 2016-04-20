# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import glitter.assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('glitter_assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('background_colour', models.CharField(blank=True, max_length=20, choices=[('red', 'Red'), ('blue', 'Blue'), ('purple', 'Purple'), ('dark-green', 'Dark Green'), ('green', 'Green'), ('yellow', 'Yellow')])),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('link_text', models.CharField(blank=True, max_length=100)),
                ('new_window', models.BooleanField(verbose_name='Open link in new window', default=False)),
                ('background_image', glitter.assets.fields.AssetForeignKey(null=True, related_name='+', blank=True, to='glitter_assets.Image')),
                ('content_block', models.ForeignKey(editable=False, null=True, to='glitter.ContentBlock')),
                ('image', glitter.assets.fields.AssetForeignKey(null=True, related_name='+', to='glitter_assets.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
