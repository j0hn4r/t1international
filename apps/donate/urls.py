from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^one-time/$',
        views.DonatePageView.as_view(),
        name='donate-page'),
    url(r'^one-time/complete/$',
        views.DonateCompleteView.as_view(),
        name='donate-complete'),

    url(r'^subscribe/$',
        views.SubscribePageView.as_view(),
        name='subscribe-page'),
    url(r'^subscribe/complete/$',
        views.SubscribeCompleteView.as_view(),
        name='subscribe-complete'),

    url(r'^success/$',
        views.donate_glitterpage,
        name='donate-success'),
    url(r'^failed/$',
        views.donate_glitterpage,
        name='donate-failed'),
]
