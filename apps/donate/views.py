# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import FormView
from glitter.pages.views import glitter
import stripe

from .forms import DonationCompleteForm, SubscriberCompleteForm


class BaseCompleteView(FormView):
    @method_decorator(require_POST)
    def dispatch(self, *args, **kwargs):
        return super(BaseCompleteView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)

        try:
            self.complete_order(obj=obj, token=form.cleaned_data['token'])

            # Update order
            obj.save()

            return redirect('donate:donate-success')
        except stripe.CardError:
            pass

        # Something went wrong, so just go with form_invalid!
        return self.form_invalid(form)

    def form_invalid(self, form):
        return redirect('donate:donate-failed')

    def customer_metadata(self, obj):
        return {
            'no_donating_email': obj.no_donating_email,
            'no_updates_email': obj.no_updates_email,
        }


class DonateCompleteView(BaseCompleteView):
    form_class = DonationCompleteForm

    def complete_order(self, obj, token):
        customer = stripe.Customer.create(
            api_key=settings.STRIPE_SECRET_KEY,
            source=token,
            email=obj.email,
            metadata=self.customer_metadata(obj=obj))

        # One-off charge
        stripe.Charge.create(
            api_key=settings.STRIPE_SECRET_KEY,
            amount=obj.amount_pence,
            currency=settings.DONATE_CURRENCY,
            customer=customer,
            description='Donation')


class SubscribeCompleteView(BaseCompleteView):
    form_class = SubscriberCompleteForm

    def complete_order(self, obj, token):
        customer = stripe.Customer.create(
            api_key=settings.STRIPE_SECRET_KEY,
            source=token,
            email=obj.email,
            metadata=self.customer_metadata(obj=obj))

        # Recurring subscription
        stripe.Subscription.create(
            api_key=settings.STRIPE_SECRET_KEY,
            plan=obj.plan.stripe_id,
            customer=customer)


def donate_glitterpage(request):
    return glitter(request, request.path)
