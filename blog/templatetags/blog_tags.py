from django import template
from blog.models import Post, Comment, Category

# Defining registration object
register = template.Library()

