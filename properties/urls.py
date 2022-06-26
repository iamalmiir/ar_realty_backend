from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from properties import views

urlpatterns = [
    path("properties/", views.PropertyList.as_view()),
    path("properties/<slug:slug>/", views.PropertyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
