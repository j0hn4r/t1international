from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^one-time/$',
        views.DonateCompleteView.as_view(),
        name='donate-complete'),
    url(r'^subscribe/$',
        views.SubscribeCompleteView.as_view(),
        name='subscribe-complete'),

    url(r'^success/$',
        views.donate_glitterpage,
        name='donate-success'),
    url(r'^failed/$',
        views.donate_glitterpage,
        name='donate-failed'),
]
