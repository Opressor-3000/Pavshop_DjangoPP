from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.db.models import Q, Sum, Count, F
from django.views.generic import ListView, DetailView, CreateView
from django.db.models.query import QuerySet


from .models import Post, PostReview
from account.models import User
from product.models import Tag, Category


class PostList(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'postlist'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        posts = Post.objects.all()
        context['blog_recent'] = posts.order_by('-created_at')[:3]
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.annotate(cat = Sum('categories')).order_by('cat')[:8]
        context['tags'] = Tag.objects.annotate(count1 = Count(F('tags'))).filter(count1__gt=0)
        context['count_review'] = posts.annotate(count2 = Count('post')).filter(count2__gt=0)
        context['review_count'] = PostReview.objects.annotate(Count('post'))
        
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Post.objects.all()
        if self.request.method == 'GET':
            req = self.request.GET
            if req.get('search'):
                queryset.filter(
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
            if req.get('tag'):
                return queryset.filter(tag__in=req.get('tags'))[:7]
            if req.get('new_post'):
                return queryset.order_by('-created_at')
            if req.get('user'):
                user = User.objects.annotate(userid = Count('author')).filter(userid__gt=0)
            return queryset.filter(author=req.get(user))

    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['blog_recent'] = posts.order_by('-created_at')[:3]
        context['category'] = Category.objects.annotate(cat = Sum('categories')).order_by('cat')[:8]
        context['tags'] = Tag.objects.filter()
        context['tag_count'] = context['tags'].annotate(count1 = Count(F('tags'))).filter(count1__gt=0)
        context['count_review'] = posts.annotate(count2 = Count('post')).filter(count2__gt=0)
        post_review = PostReview.objects.all()
        context['review_count'] = post_review.annotate(Count('post'))
        context['post_reviews'] = post_review.filter(post=self.queryset).order_by('created_at')
        return context
    
# OrderProduct.objects.filter(product=product).aggregate(... total=Sum(F('total_products'), output_field=IntegerField()) 
# {'total': 123}

# product_list = Product.objects.annotate(total_votes=Sum('vote__score')).order_by('total_votes')

# {{ car.date_of_manufacture|format_datetime }}
# {{ car.date_of_manufacture|format_datetime('full') }}