from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout, get_user_model


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                remember = form.cleaned_data.get('remember_me')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'You are now logged in!')
                    if not remember:
                        request.session.set_expiry(0)
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Your entered information was wrong!')
                return render(request, 'accounts/login.html', {'form': form})
        else:
            form = UserLoginForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    else:
        messages.add_message(request, messages.WARNING, "You are already logged In.")
        return redirect('/')
