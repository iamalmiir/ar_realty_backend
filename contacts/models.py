from uuid import uuid4

from django.db import models

from users.models import User


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    listing = models.CharField(max_length=100)
    listing_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name
