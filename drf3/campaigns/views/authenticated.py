from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from campaigns.models import Campaign
from campaigns.permissions import IsOwnerOrReadOnly
from campaigns.serializers import CampaignSerializer, UserSerializer


class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """Used instead of the deprecated `pre_save`."""
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer