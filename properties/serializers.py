from rest_framework import serializers

from properties.models import Property
from realtors.serializers import RealtorSerializer


class PropertySerializer(serializers.ModelSerializer):
    realtor = RealtorSerializer(read_only=True)

    class Meta:
        model = Property
        fields = "__all__"
