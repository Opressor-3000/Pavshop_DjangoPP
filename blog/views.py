from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.db.models import Q
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
        return queryset

    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    