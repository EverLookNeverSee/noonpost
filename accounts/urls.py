from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import login_view, logout_view, signup_view, EmailValidationOnForgotPassword
