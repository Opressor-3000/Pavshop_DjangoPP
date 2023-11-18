from django import template
from django.db.models import Count


from blog.models import Post
from product.models import Category, Tag
register = template.Library()

@register.simple_tag
def get_search_post(request):
   return 

@register.inclusion_tag('partials/sider_bar.py')
def get_blogsidebar():
   blog_cats = Category.objects.annotate(cat = Count('categories')).order_by('cat').distinct()
   blog_tags = Tag.objects.annotate(tag = Count('tags')).order_by('tag').distinct()
   blog_recents = Post.objects.annotate(recent = Count('postreview')).order_by('recent')[:3]
   blogside = {'blog_cats': blog_cats, 'blog_tags': blog_tags, 'blog_recents': blog_recents }
   return blogside

@register.simple_tag
def get_blogcat():
   return Category.objects.annotate(cat = Count('categories')).order_by('cat').distinct()[:8]

@register.simple_tag
def get_blogtag():
   return Tag.objects.annotate(tag = Count('tags')).order_by('tag').distinct()[:7]

@register.simple_tag
def get_postrecent():
   return Post.objects.all()[:3]