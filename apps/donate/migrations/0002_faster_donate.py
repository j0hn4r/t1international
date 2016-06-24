# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='secret_key',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='success',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='secret_key',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='success',
        ),
        migrations.RemoveField(
            model_name='subscriberplan',
            name='order',
        ),
        migrations.AlterField(
            model_name='donation',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]
