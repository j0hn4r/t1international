from __future__ import absolute_import

from django.contrib import admin

from .models import Donation, Subscriber, SubscriberPlan


# Note: intentionally hidden, Stripe is the authoritative source


# @admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'amount', 'created')
    list_filter = ('created',)
    search_fields = ('email_address',)
    date_hierarchy = 'created'


# @admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created')
    list_filter = ('created', 'plan')
    search_fields = ('email_address',)
    date_hierarchy = 'created'


# @admin.register(SubscriberPlan)
class SubscriberPlanAdmin(admin.ModelAdmin):
    pass
