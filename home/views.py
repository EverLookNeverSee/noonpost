from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm


def index_view(request):
    return render(request, "home/index.html")


def about_view(request):
    return render(request, "home/about.html")


def contact_view(request):
    return render(request, "home/contact.html")


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
