from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout, get_user_model
