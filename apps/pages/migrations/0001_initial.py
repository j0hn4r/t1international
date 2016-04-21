# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockquote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('citation', models.CharField(max_length=256)),
                ('background_color', models.CharField(max_length=16, choices=[('red', 'Red'), ('blue', 'Blue'), ('purple', 'Purple'), ('dark-green', 'Dark Green')])),
                ('content_block', models.ForeignKey(editable=False, to='glitter.ContentBlock', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
