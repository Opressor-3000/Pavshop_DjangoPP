from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.db.models import Q, Sum, Count
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Post
from account.models import User


class PostList(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'postlist'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Post.objects.all()
        if self.request.method == 'GET':
            req = self.request.GET
            if req.get('search'):
                return queryset.filter(
                    Q(title__icontains=req.get['search']) | 
                    Q(product__icontains=req.get['search']) |
                    Q(tag__icontains=req.get['search']) |
                    Q(author__icontains=req.get['search'])
                ).distinct
            if req.getlist('taglist'):
                queryset.filter(tag_in=req.getlist('taglist'))
            if req.get('popular'):
                return queryset.annotate(total_count = Count('postreview')).order_by('total_count')
            if req.get('category'):
                return queryset.filter(category__in=req.get('category'))[:10]
            if req.get('tags'):
                return queryset.filter(tag__in=req.get('tags'))[:7]
            if req.get('new_post'):
                return queryset.order_by('-created_at')
            if req.get('user'):
                user = User.objects.filter()
                return queryset.filter(author=req.get(user))

    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['review_count'] = QuerySet.postreview.count()
        posts = Post.objects.all()
        context['category'] = posts.aggregate(cat = Sum('categories')).order_by('cat')
        context['tags'] = posts.aggregate(tag = Sum('tags')).order_by('tag')
        context['resent_post'] = posts.aggregate(recent = Sum('postreview')).order_by('postreview')
        return context