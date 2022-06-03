from users import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
