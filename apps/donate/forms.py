# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, HTML, Layout
from django import forms
from django.core.urlresolvers import reverse

from .models import Donation, Subscriber, SubscriberPlan


class DonateFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(DonateFormMixin, self).__init__(*args, **kwargs)

        # Multiple URLs for slightly different forms
        onetime_url = reverse('donate:donate-page')
        subscribe_url = reverse('donate:subscribe-page')

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                """
                Lorem ipsum. Replace this textum.
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
                id='donate-form', css_class='donate-form'
            )
        )


class DonationForm(DonateFormMixin, forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('amount',)


class DonationCompleteForm(forms.Form):
    obj = forms.ModelChoiceField(
        queryset=Donation.objects.filter(success=False), widget=forms.HiddenInput)
    secret_key = forms.CharField(widget=forms.HiddenInput)
    token = forms.CharField(widget=forms.HiddenInput)
    email = forms.EmailField(widget=forms.HiddenInput)


class SubscriberForm(DonateFormMixin, forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('amount',)

    amount = forms.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        # Fix the plan based on the amount
        amount = self.cleaned_data['amount']
        self.instance.plan = SubscriberPlan.get_plan(amount=amount)

        return super(SubscriberForm, self).save(*args, **kwargs)


class SubscriberCompleteForm(forms.Form):
    obj = forms.ModelChoiceField(
        queryset=Subscriber.objects.filter(success=False), widget=forms.HiddenInput)
    secret_key = forms.CharField(widget=forms.HiddenInput)
    token = forms.CharField(widget=forms.HiddenInput)
    email = forms.EmailField(widget=forms.HiddenInput)
