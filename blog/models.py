from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
