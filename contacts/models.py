from uuid import uuid4

from django.db import models

from properties.models import Listing
from users.models import User


class Inquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    listing = models.CharField(max_length=100)
    listing_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=255)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(blank=True, null=True)

    def __str__(self):
        return self.name


class BusinessInquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=255)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
