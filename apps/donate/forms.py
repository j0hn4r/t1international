# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, HTML, Layout
from django import forms
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from .models import Donation, Subscriber, SubscriberPlan


class DonationForm(forms.Form):
    amount = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)

        # Multiple URLs for slightly different forms
        onetime_url = reverse('donate:donate-complete')
        subscribe_url = reverse('donate:subscribe-complete')

        self.helper = FormHelper()
        self.helper.form_id = 'donate-form'
        self.helper.disable_csrf = True
        self.helper.attrs = {
            'data-stripe': settings.STRIPE_PUBLIC_KEY,
            'data-image': staticfiles_storage.url('img/stripe.png'),
            'data-currency': settings.DONATE_CURRENCY,
            'data-symbol': settings.DONATE_SYMBOL,
        }
        self.helper.layout = Layout(
            Fieldset(
                """
                My donation to T1International
                """,
                'amount',
                HTML(
                    """
                    <button type="submit" class="donate-button donate-onetime" data-url="{}">
                        One-time donation
                    </button>
                    <button type="submit" class="donate-button donate-monthly" data-url="{}">
                        Monthly donation
                    </button>
                    """.format(onetime_url, subscribe_url)),
                css_class='donate-form'
            )
        )


class DonationCompleteForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('amount', 'email', 'token')

    token = forms.CharField(widget=forms.HiddenInput)


class SubscriberCompleteForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

    amount = forms.IntegerField(min_value=1)
    token = forms.CharField(widget=forms.HiddenInput)

    def save(self, *args, **kwargs):
        # Fix the plan based on the amount
        amount = self.cleaned_data['amount']
        self.instance.plan = SubscriberPlan.get_plan(amount=amount)

        return super(SubscriberCompleteForm, self).save(*args, **kwargs)
