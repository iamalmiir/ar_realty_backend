from rest_framework import permissions
from rest_framework import generics
from properties.models import Property
from properties.serializers import PropertySerializer


class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)