from django.contrib import admin
from properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["realtor", "title", "is_published"]
    list_filter = ["realtor", "is_published"]
    search_fields = ["title", "description"]
    list_per_page = 25
