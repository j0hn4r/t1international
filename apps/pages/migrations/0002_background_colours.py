# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockquote',
            name='background_color',
            field=models.CharField(max_length=16, choices=[('red', 'Red'), ('blue', 'Blue'), ('purple', 'Purple'), ('dark-green', 'Dark Green'), ('green', 'Green'), ('yellow', 'Yellow')]),
        ),
    ]
