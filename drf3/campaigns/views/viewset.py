from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from campaigns.models import Campaign
from campaigns.permissions import IsOwnerOrReadOnly
from campaigns.serializers import CampaignSerializer, UserSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer