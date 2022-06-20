from datetime import datetime
from uuid import uuid4

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from realtors.models import Realtor

PROPERTY_PHOTOS = 'photos/%Y/%m/%d/'


class Property(models.Model):
    realtor = models.ForeignKey(
        Realtor,
        on_delete=models.CASCADE,
        related_name="properties",
    )
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4,
        editable=False,
    )
    slug = models.SlugField(editable=False, unique=True, max_length=50, null=True, blank=True)
    title = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)

    # Media
    photo_main = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)
    photo_1 = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)
    photo_2 = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)
    photo_3 = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)
    photo_4 = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)
    photo_5 = models.ImageField(upload_to=PROPERTY_PHOTOS, blank=True)

    is_published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("title", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.title + "-" + str(self.realtor.full_name)
        self.slug = slugify(
            value,
        )
        super().save(*args, **kwargs)
