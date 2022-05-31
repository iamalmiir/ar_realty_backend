from rest_framework import serializers
from properties.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            "ID",
            "slug",
            "title",
            "address",
            "city",
            "state",
            "zipcode",
            "description",
            "price",
            "bedrooms",
            "bathrooms",
            "garage",
            "sqft",
            "lot_size",
            "photo_main",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "photo_5",
            "is_published",
            "pub_date",
            "realtor",
        ]
