from rest_framework import generics
from rest_framework import permissions

from properties.models import Listing
from properties.serializers import ListingSerializer


class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()

    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Get the Property object by filtering by slug
class ListingDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = ListingSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Listing.objects.filter(slug=slug)
