from django import template
from ..models import Signee


register = template.Library()


@register.assignment_tag
def get_signees():
    return Signee.objects.all()
