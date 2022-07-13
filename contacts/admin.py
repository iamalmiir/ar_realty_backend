from django.contrib import admin

from contacts.models import Inquiry


@admin.register(Inquiry)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("listing", "name", "email", "phone")
    list_display_links = (
        "listing",
        "name",
        "email",
        "phone",
    )
    search_fields = ("listing", "listing_id", "name", "email", "phone", "message", "user_id")
    list_per_page = 25
