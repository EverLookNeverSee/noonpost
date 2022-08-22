from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import login_view, logout_view, signup_view, EmailValidationOnForgotPassword


# Defining appname
app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]
