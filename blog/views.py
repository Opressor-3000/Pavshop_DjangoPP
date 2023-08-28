from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    


# def blog_detail(request):
#     return render("blog_detail.html")

# def blog_list(request):
#     return H("blog_list.html")