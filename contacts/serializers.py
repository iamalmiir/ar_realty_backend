from rest_framework import serializers

from contacts.models import Inquiry, BusinessInquiry
from properties.serializers import ListingSerializer


class InquirySerializer(serializers.ModelSerializer):
    listing_details = ListingSerializer(read_only=True, many=True)

    class Meta:
        model = Inquiry
        fields = "__all__"


class BusinessInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInquiry
        fields = "__all__"
