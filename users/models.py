from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

DEFAULT_AVATAR_URL = (
    "https://res.cloudinary.com/iamalmiir/image/upload/v1657350671/catAvatar_iakq5p.jpg"
)


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, full_name, password):
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            full_name=full_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, full_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            user_name=user_name,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.user_name = user_name
        user.first_name = full_name
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    default_avatar = models.CharField(max_length=255, default=DEFAULT_AVATAR_URL)
    email = models.EmailField(
        _("email address"),
        max_length=50,
        unique=True,
    )
    user_name = models.CharField(
        _("user name"),
        max_length=15,
        unique=True,
    )
    full_name = models.CharField(
        _("full name"),
        max_length=100,
    )
    photo = models.ImageField(_("profile picture"), blank=True)
    start_date = models.DateTimeField(
        _("start date"),
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    objects = CustomAccountManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return self.user_name
