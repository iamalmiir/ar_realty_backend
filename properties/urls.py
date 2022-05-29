from properties import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("properties/", views.PropertyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
