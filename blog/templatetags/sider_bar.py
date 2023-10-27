from django import template
from django.db.models import Count


from blog.models import Post
from product.models import Category, Tag
register = template.Library()

@register.simple_tag
def get_search_post(request):
   return 

@register.inclusion_tag('partials/sider_bar.py')
def get_blog_sidebar():
   blog_cats = Category.objects.annotate(cat = Count('categories')).order_by('cat')
   print('sdfghjkll;oilukyjthrvedcvgbnhyj', blog_cats)
   blog_tags = Tag.objects.annotate(tag = Count('tags')).order_by('tag')
   blog_recents = Post.objects.annotate(recent = Count('postreview')).order_by('recent')[:3]
   return {'blog_cats': blog_cats, 'blog_tags': blog_tags, 'blog_recents': blog_recents }
