# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('blocks', '0002_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_block', models.ForeignKey(to='glitter.ContentBlock', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
