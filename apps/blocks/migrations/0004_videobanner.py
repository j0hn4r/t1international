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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('background_video', glitter.assets.fields.AssetForeignKey(null=True, to='glitter_assets.File')),
                ('content_block', models.ForeignKey(editable=False, null=True, to='glitter.ContentBlock')),
                ('fallback_image', glitter.assets.fields.AssetForeignKey(null=True, to='glitter_assets.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
