from django.urls import reverse
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib import messages
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_index(request):
    return render(request, "blog/blog-home.html")


def blog_single(request):
    return render(request, "blog/blog-single.html")
