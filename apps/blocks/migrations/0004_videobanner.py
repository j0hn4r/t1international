# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import glitter.assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('glitter_assets', '0001_initial'),
        ('blocks', '0003_signees'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField()),
                ('background_video', glitter.assets.fields.AssetForeignKey(to='glitter_assets.File', null=True, blank=True)),
                ('content_block', models.ForeignKey(editable=False, null=True, to='glitter.ContentBlock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
