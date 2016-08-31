# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import glitter.assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glitter_assets', '0001_initial'),
        ('blocks', '0004_videobanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='videobanner',
            name='fallback_image',
            field=glitter.assets.fields.AssetForeignKey(null=True, to='glitter_assets.Image'),
        ),
        migrations.AlterField(
            model_name='videobanner',
            name='background_video',
            field=glitter.assets.fields.AssetForeignKey(null=True, to='glitter_assets.File'),
        ),
    ]
