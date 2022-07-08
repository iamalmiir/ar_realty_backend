from rest_framework import generics
from rest_framework import permissions

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserContactList(generics.RetrieveAPIView):
    lookup_field = "user_id"
    serializer_class = ContactSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Contact.objects.filter(user_id=user_id)
