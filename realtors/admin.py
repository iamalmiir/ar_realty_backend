from django.contrib import admin
from realtors.models import Realtor


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "is_mvp"]
