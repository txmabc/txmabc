from django.urls import path

from portal.views import index

app_name = "portal"
urlpatterns = [
    path("", index.index, name="index"),
]
