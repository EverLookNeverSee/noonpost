from django import template
from blog.models import Post, Comment, Category

# Defining registration object
register = template.Library()



@register.simple_tag(name="n_published_posts")
def get_number_of_published_posts() -> int:
    """
    Get the number of published posts - ok_to_publish filed is True
    :return: int, number of published posts
    """
    return Post.objects.filter(ok_to_publish=True).count()
