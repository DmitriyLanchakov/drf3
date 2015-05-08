from django.conf.urls import include, url

from campaigns.views import generic_class_based

urlpatterns = [
    url(r'^campaigns/$', generic_class_based.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', generic_class_based.CampaignDetail.as_view()),
]
