from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.db.models import Q, Sum, Count
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Post


class PostList(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'postlist'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        req = self.request.GET
        if req.get['search']:
            queryset = queryset.filter(
                Q(title__icontains=req.get['search']) | 
                Q(product__icontains=req.get['search']) |
                Q(tag__icontains=req.get['search']) |
                Q(author__icontains=req.get['search'])
            ).distinct
        if req.get['new']:
            queryset.order_by('created_at')
        if req.get['popular']:
            queryset = queryset.annotate(total_count = Count('postreview')).order_by('total_count')
        return queryset

    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['review_count'] = QuerySet.postreview.count()
        posts = Post.objects.all()
        context['category'] = posts.aggregate(cat = Sum('categories')).order_by('cat')
        context['tags'] = posts.aggregate(tag = Sum('tags')).order_by('tag')
        context['resent_post'] = posts.aggregate(recent = Sum('postreview')).order_by('postreview')
        return context