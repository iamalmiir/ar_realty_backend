from rest_framework import generics
from rest_framework import permissions

from properties.models import Property
from properties.serializers import PropertySerializer


class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()

    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Get the Property object by filtering by slug
class PropertyDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = PropertySerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Property.objects.filter(slug=slug)
