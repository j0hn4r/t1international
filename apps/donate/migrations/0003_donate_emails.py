# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_faster_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='no_donating_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donation',
            name='no_updates_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='no_donating_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='no_updates_email',
            field=models.BooleanField(default=False),
        ),
    ]
