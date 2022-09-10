from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.conf import settings
import urllib
import json


def index_view(request):
    return render(request, "home/index.html")


def about_view(request):
    return render(request, "home/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Your message has been sent!')
            else:
                messages.add_message(request, messages.ERROR, "Invalid reCAPTCHA. Please try again.")
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent!')
    form = ContactForm()
    PUBLIC_KEY = settings.RECAPTCHA_PUBLIC_KEY
    context = {'form': form, 'PUBLIC_KEY': PUBLIC_KEY}
    return render(request, "home/contact.html", context)


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You subscribed to newsletter successfully.')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Your subscription was not successful.')
    else:
        return HttpResponseRedirect('/')
