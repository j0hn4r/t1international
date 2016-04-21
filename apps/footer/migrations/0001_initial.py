# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('link', models.URLField()),
                ('sort_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
