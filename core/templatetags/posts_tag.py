from django.db.models import Count
from django import template


from blog.models import Post
from account.models import User

register = template.Library()

@register.simple_tag
def get_posts():
    result = User.objects.annotate(users = Count('author')).filter(users__gt=0)
    return result