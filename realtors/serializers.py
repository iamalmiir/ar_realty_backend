from rest_framework import serializers
from realtors.models import Realtor
from django.contrib.auth.models import User


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ["ID", "slug", "full_name", "photo", "description", "phone", "email", "is_mvp"]
