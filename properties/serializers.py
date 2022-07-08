from rest_framework import serializers

from properties.models import Listing
from realtors.serializers import RealtorSerializer


class ListingSerializer(serializers.ModelSerializer):
    realtor = RealtorSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = "__all__"
