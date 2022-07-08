from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from properties import views

urlpatterns = [
    path("properties/", views.ListingList.as_view()),
    path("properties/<slug:slug>/", views.ListingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
