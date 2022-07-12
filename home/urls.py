from django.urls import path
from home.views import index_view

# Defining app name
app_name = "website"

urlpatterns = [
    path("", index_view, name="index"),
]
