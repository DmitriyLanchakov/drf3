from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers

from campaigns.models import Campaign, CAMPAIGN_TYPES


"""
These aren't actually used i this app; only here 
as demontration of how the `ModelSerializer` works.
"""
class CampaignSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField()
    user = serializers.Field(source='user.username')

    def create(self, validated_data):
        """
        Create and return a new `Campaign` instances comprised of the validated data.
        """
        return Campaign.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Campaign` instance
        based on the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    campaigns = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'campaigns')