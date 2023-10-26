from django.db.models import Count
from django import template


from blog.models import Post
from account.models import User

register = template.Library()

@register.simple_tag
def get_posts(request):
    return User.objects.annotate(users = Count('blog__author'))