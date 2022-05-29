from django.contrib import admin
from realtors.models import Realtor


# class RealtorAdmin(admin.ModelAdmin):
#     list_display = ("id", "full_name", "hire_date")
#     list_display_links = ("id", "full_name")
#     search_fields = ("full_name",)
#     list_per_page = 25


admin.site.register(Realtor)
