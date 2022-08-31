from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_at"
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'count_views', 'ok_to_publish', 'created_at', 'published_date')
    list_filter = ('author', 'ok_to_publish', 'created_date', 'publish_date')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at', 'post')
    search_fields = ('name', 'post')
