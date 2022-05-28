from realtors.models import Realtor
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from realtors.serializers import RealtorSerializer


class RealtorList(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
