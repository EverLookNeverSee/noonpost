from django import template
from blog.models import Post, Comment, Category
from typing import List, Dict

# Defining registration object
register = template.Library()



@register.simple_tag(name="n_published_posts")
def get_number_of_published_posts() -> int:
    """
    Get the number of published posts - ok_to_publish filed is True
    :return: int, number of published posts
    """
    return Post.objects.filter(ok_to_publish=True).count()


@register.simple_tag(name="published_posts")
def get_published_posts() -> List[Post]:
    """
    Get the list of published posts - ok_to_publish filed is True
    :return: List, published posts
    """
    return Post.objects.filter(ok_to_publish=True)


@register.filter
def summary(value, word_count) -> str:
    """
    Summarizing the string
    :param value: str, string object
    :param word_count: int, first word_count number of characters
    :return: str, summarized string
    """
    return f"{value[:word_count]}..."


@register.inclusion_tag("blog/blog-latest-posts.html")
def blog_latest_posts(count=6) -> Dict[str, List[Post]]:
    """
    Latest published posts
    :param count: int, number of the latest posts that we want to return
    :return: List, latest published posts
    """
    posts = Post.objects.filter(ok_to_publish=True).order_by("-publish_date")[:count]
    return {"posts": posts}


@register.inclusion_tag("home/footer_recent_posts.html")
def footer_recent_posts(count=3) -> Dict[str, List[Post]]:
    """
        Latest published posts for footer section
        :param count: int, number of the latest posts that we want to return
        :return: List, latest published posts
        """
    posts = Post.objects.filter(ok_to_publish=True).order_by("-publish_date")[:count]
    return {"posts": posts}


@register.inclusion_tag("home/latest_posts.html")
def home_latest_posts(count=6) -> Dict[str, List[Post]]:
    """
    Latest published posts for home page
    :param count: int, number of the latest posts that we want to return
    :return: List, latest published posts
    """
    posts = Post.objects.filter(ok_to_publish=True).order_by("-publish_date")[:count]
    return {"posts": posts}


@register.inclusion_tag("blog/blog-posts-categories.html")
def posts_categories() -> Dict[str, Dict]:
    """
    Posts categories
    :return: dict, posts categories
    """
    posts = Post.objects.filter(ok_to_publish=True)
    categories = Category.objects.all()
    cat_dict = dict()
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}


@register.inclusion_tag("home/all_categories.html")
def all_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.simple_tag(name="comments_count")
def get_comments_count(pid) -> int:
    """
    Get the number of approved comments of a post
    :param pid: Post id
    :return: int, number of approved comments of the post
    """
    return Comment.objects.filter(post=pid, is_approved=True).count()


@register.inclusion_tag("home/top_viewed_posts.html")
def top_viewed_posts(count=3) -> Dict[str, List[Post]]:
    """
    Top viewed posts
    :param count: int, number of top viewed posts that we want to return
    :return: List, top viewed posts
    """
    posts = Post.objects.filter(ok_to_publish=True).order_by("-count_views")[:count]
    return {"posts": posts}
