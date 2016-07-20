# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, transaction
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

import stripe


@python_2_unicode_compatible
class Donation(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    email = models.EmailField(db_index=True)
    created = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Donation #%d' % (self.id,)

    @property
    def amount_pence(self):
        return int(self.amount * 100)


@python_2_unicode_compatible
class SubscriberPlan(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    amount = models.DecimalField(
        max_digits=9, decimal_places=2, help_text='Monthly amount', unique=True)
    stripe_id = models.CharField('Stripe ID', max_length=100, unique=True)

    def __str__(self):
        return self.title

    @property
    def amount_pence(self):
        if self.amount:
            return int(self.amount * 100)
        else:
            return None

    @classmethod
    def get_plan(cls, amount):
        try:
            return SubscriberPlan.objects.get(amount=amount)
        except cls.DoesNotExist:
            pass

        # Need to create the plan with Stripe
        with transaction.atomic():
            obj = SubscriberPlan(amount=amount)

            # Let the field format things appropriately
            obj.title = '£%s Monthly Donation' % (obj.amount,)
            obj.stripe_id = '%d-GBP-MONTHLY-DONATION' % (obj.amount_pence,)

            # Create the plan in Stripe first
            stripe.Plan.create(
                api_key=settings.STRIPE_SECRET_KEY,
                amount=obj.amount_pence,
                interval='month',
                name=obj.title,
                currency='GBP',
                id=obj.stripe_id)

            # Then save it
            obj.save()

        return obj


@python_2_unicode_compatible
class Subscriber(models.Model):
    plan = models.ForeignKey(SubscriberPlan)
    email = models.EmailField(db_index=True)
    created = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Subscriber #%d' % (self.id,)
