from django.db import models


class Realtor(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="realtors/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
