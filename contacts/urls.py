from contacts import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("contacts/", views.ContactList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
