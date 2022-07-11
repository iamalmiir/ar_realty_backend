from rest_framework import generics
from rest_framework import permissions

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)
