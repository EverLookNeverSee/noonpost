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
