# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from crispy_forms.utils import render_crispy_form
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import FormView
from glitter.pages.views import glitter
import stripe

from .forms import DonationCompleteForm, DonationForm, SubscriberCompleteForm, SubscriberForm


class BaseDonateView(FormView):
    @method_decorator(require_POST)
    def dispatch(self, *args, **kwargs):
        return super(BaseDonateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseDonateView, self).get_context_data(**kwargs)
        context['complete_form'] = self.complete_form_class()
        context['complete_url'] = self.complete_url
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context

    def post(self, request, *args, **kwargs):
        """ Only accept responses from Javascript. """
        if not request.is_ajax():
            raise PermissionDenied

        return super(BaseDonateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()

        return JsonResponse({
            'success': True,
            'id': obj.id,
            'public_key': settings.STRIPE_PUBLIC_KEY,
            'secret_key': obj.secret_key,
            'stripe_open': self.stripe_open(obj),
            'complete_url': reverse(self.complete_url),
        })

    def stripe_open(self, obj):
        return {
            'name': 'T1International',
            'image': staticfiles_storage.url('img/stripe.png'),
            'billingAddress': True,
            'shippingAddress': False,
        }

    def form_invalid(self, form):
        return JsonResponse({
            'success': False,
            'form': render_crispy_form(form, context=csrf(self.request)),
        })


class BaseCompleteView(FormView):
    @method_decorator(require_POST)
    def dispatch(self, *args, **kwargs):
        return super(BaseCompleteView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.cleaned_data['obj']

        if obj.valid_order(secret_key=form.cleaned_data['secret_key']):
            try:
                self.complete_order(
                    obj=obj, token=form.cleaned_data['token'], email=form.cleaned_data['email'])

                # Update order
                obj.paid = timezone.now()
                obj.success = True
                obj.email = form.cleaned_data['email']
                obj.save()

                # Emails
                self.email_admins(obj)
                self.email_user(obj)

                return redirect('donate:donate-success')
            except stripe.CardError:
                pass

        # Something went wrong, so just go with form_invalid!
        return self.form_invalid(form)

    def form_invalid(self, form):
        return redirect('donate:donate-failed')

    def email_admins(self, obj):
        pass

    def email_user(self, obj):
        pass


class DonatePageView(BaseDonateView):
    form_class = DonationForm
    complete_form_class = DonationCompleteForm
    complete_url = 'donate:donate-complete'

    def stripe_open(self, obj):
        stripe_dict = super(DonatePageView, self).stripe_open(obj)
        stripe_dict.update({
            'description': 'Donation - £%s' % (obj.amount,),
            'amount': obj.amount_pence,
            'currency': 'GBP',
        })
        return stripe_dict


class DonateCompleteView(BaseCompleteView):
    form_class = DonationCompleteForm

    def complete_order(self, obj, token, email):
        customer = stripe.Customer.create(
            api_key=settings.STRIPE_SECRET_KEY,
            source=token,
            email=email)

        # One-off charge
        stripe.Charge.create(
            api_key=settings.STRIPE_SECRET_KEY,
            amount=obj.amount_pence,
            currency='GBP',
            customer=customer,
            description='Donation')


class SubscribePageView(BaseDonateView):
    form_class = SubscriberForm
    complete_form_class = SubscriberCompleteForm
    complete_url = 'donate:subscribe-complete'

    def stripe_open(self, obj):
        stripe_dict = super(SubscribePageView, self).stripe_open(obj)
        stripe_dict.update({
            'description': obj.plan.title,
            'panelLabel': 'Subscribe',
        })
        return stripe_dict


class SubscribeCompleteView(BaseCompleteView):
    form_class = SubscriberCompleteForm

    def complete_order(self, obj, token, email):
        customer = stripe.Customer.create(
            api_key=settings.STRIPE_SECRET_KEY,
            source=token,
            email=email)

        # Recurring subscription
        stripe.Subscription.create(
            api_key=settings.STRIPE_SECRET_KEY,
            plan=obj.plan.stripe_id,
            customer=customer)


def donate_glitterpage(request):
    return glitter(request, request.path)
