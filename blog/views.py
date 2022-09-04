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


def increment_views(pid):
    post = get_object_or_404(Post, id=pid)
    post.count_views += 1
    post.save()


def get_previous_next_posts(pid):
    post = get_object_or_404(Post, id=pid)
    previous_post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date').filter(
        publish_date__lte=post.publish_date).exclude(id=pid).first()
    next_post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date').filter(
        publish_date__gte=post.publish_date).exclude(id=pid).last()
    return previous_post, next_post


def blog_single(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = get_object_or_404(Post, id=pid)
            new_form.save()
            messages.add_message(request, messages.SUCCESS, "Comment added successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Error adding comment!")
    post = get_object_or_404(Post, id=pid, ok_to_publish=True, publish_date__lte=timezone.now())
    if post.login_required is False:
        comments = Comment.objects.filter(post=post.id, is_approved=True)
        increment_views(pid)
        form = CommentForm()
        context = {"post": post, "comments:": comments, "form": form}
        previous_post, next_post = get_previous_next_posts(pid)
        if previous_post:
            context["previous_post"] = previous_post
        if next_post:
            context["next_post"] = next_post
        return render(request, "blog/blog-single.html", context)
    else:
        return HttpResponseRedirect(reverse("accounts:login"))
