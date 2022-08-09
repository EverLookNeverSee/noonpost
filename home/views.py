from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, "home/index.html")


def about_view(request):
    return render(request, "home/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent!')
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent!')
    form = ContactForm()
    return render(request, "home/contact.html", {'form': form})


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
