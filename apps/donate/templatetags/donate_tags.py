from django import template

from ..forms import DonationForm, DonationCompleteForm

register = template.Library()


@register.assignment_tag
def get_donate_form():
    return DonationForm()


@register.assignment_tag
def get_complete_form():
    return DonationCompleteForm(auto_id=False)
