from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


# @admin.register(NewUser)
class UserAdminConfig(UserAdmin):
    list_display = ("email", "user_name", "full_name", "is_staff", "is_superuser", "is_active")
    list_filter = ("email", "is_staff", "is_superuser", "is_active")
    search_fields = ("email", "user_name", "full_name")
    ordering = ("-start_date",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("user_name", "full_name", "start_date")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "20"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }


admin.site.register(NewUser, UserAdminConfig)
