from django.conf.urls import include, url

from campaigns.views import browseable

urlpatterns = [
    url(r'^campaigns/$', browseable.campaign_list),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', browseable.campaign_detail),
]
