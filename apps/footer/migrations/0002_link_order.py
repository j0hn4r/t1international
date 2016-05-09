# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['sort_order']},
        ),
    ]
