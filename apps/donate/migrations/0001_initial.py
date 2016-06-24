# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('paid', models.DateTimeField(null=True, blank=True)),
                ('secret_key', models.CharField(editable=False, max_length=32)),
                ('success', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('paid', models.DateTimeField(null=True, blank=True)),
                ('secret_key', models.CharField(editable=False, max_length=32)),
                ('success', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='SubscriberPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True, default=0)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, unique=True, max_digits=9, help_text='Monthly amount')),
                ('stripe_id', models.CharField(unique=True, max_length=100, verbose_name='Stripe ID')),
            ],
        ),
        migrations.AddField(
            model_name='subscriber',
            name='plan',
            field=models.ForeignKey(to='donate.SubscriberPlan'),
        ),
    ]
