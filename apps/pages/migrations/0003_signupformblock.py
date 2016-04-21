# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('pages', '0002_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupFormBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_block', models.ForeignKey(editable=False, to='glitter.ContentBlock', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
