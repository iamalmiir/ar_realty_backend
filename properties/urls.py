from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from properties import views

urlpatterns = [
    path("listings/", views.ListingList.as_view()),
    path("listings/quicksearch/", views.SearchQuery.as_view()),
    path("listings/<slug:slug>/", views.ListingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
