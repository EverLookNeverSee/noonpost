from django.urls import path
from home.views import index_view, about_view

# Defining app name
app_name = "home"

urlpatterns = [
    path("", index_view, name="index"),
    path("about", about_view, name="about"),
]
