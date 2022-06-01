from contacts.models import Contact
from rest_framework import permissions
from rest_framework import generics
from contacts.serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
