from django.urls import reverse
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib import messages
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_index(request, **kwargs):
    posts = Post.objects.filter(ok_to_publish=True, publish_date__lte=timezone.now()).order_by("-publish_date")
    if kwargs.get("cat_name") is not None:
        posts = posts.filter(category__name=kwargs["cat_name"], ok_to_publish=True)
    if kwargs.get("author_username") is not None:
        posts = posts.filter(author__username=kwargs["author_username"], ok_to_publish=True)
    if kwargs.get("tag_name") is not None:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]], ok_to_publish=True)
    posts = Paginator(posts, 6)
    try:
        page_number = request.GET.get("page")
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request):
    return render(request, "blog/blog-single.html")
