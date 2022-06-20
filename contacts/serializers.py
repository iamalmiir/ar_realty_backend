from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "listing",
            "listing_id",
            "name",
            "email",
            "phone",
            "message",
            "contact_date",
            "user_id",
        ]
