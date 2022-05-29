from realtors.models import Realtor
from rest_framework import permissions
from rest_framework import generics
from realtors.serializers import RealtorSerializer


class RealtorList(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Get the Realtor object by ID
class RealtorDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
