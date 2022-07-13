from rest_framework import generics
from rest_framework import permissions

from contacts.models import Inquiry
from contacts.serializers import InquirySerializer


class InquiryList(generics.ListCreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print(self.request.data.get('name'))
        serializer.save(user=self.request.inquiry)
