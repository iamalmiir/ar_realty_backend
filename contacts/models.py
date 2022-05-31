from django.db import models


class Contact(models.Model):
    listing = models.CharField(max_length=100)
    listing_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
