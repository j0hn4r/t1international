from __future__ import absolute_import

from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Donation, Subscriber, SubscriberPlan


# Note: intentionally hidden, Stripe is the authoritative source


# @admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass


# @admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created', 'success')
    list_filter = ('success', 'created', 'plan')
    search_fields = ('email_address',)
    date_hierarchy = 'created'


# @admin.register(SubscriberPlan)
class SubscriberPlanAdmin(SortableAdmin):
    pass
