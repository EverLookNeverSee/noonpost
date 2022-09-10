from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestPostsRSSFeed(Feed):
    title = "Latest posts on my blog"
    link = "/rss/feed/"
    description = "The latest posts on my blog"

    @staticmethod
    def items():
        return Post.objects.filter(ok_to_publish=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return f"{item.content[:200]}..."
