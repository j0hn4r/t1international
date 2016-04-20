# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import glitter.assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glitter_assets', '0001_initial'),
        ('glitter', '0001_initial'),
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
                ('background_image', glitter.assets.fields.AssetForeignKey(to='glitter_assets.Image', null=True, blank=True)),
                ('content_block', models.ForeignKey(to='glitter.ContentBlock', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
