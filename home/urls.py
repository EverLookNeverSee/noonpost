from django.urls import path
from home.views import index_view, about_view, contact_view

# Defining app name
app_name = "home"

urlpatterns = [
    path("", index_view, name="index"),
    path("about", about_view, name="about"),
    path("contact", contact_view, name="contact"),
]
