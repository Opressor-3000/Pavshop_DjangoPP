from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.db.models import Q, Sum, Count, F
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy


from .forms import PostReviewForm
from .models import Post, PostReview
from account.models import User
from product.models import Tag, Category


class PostList(ListView):
    paginate_by = 2
    model = Post
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        posts = Post.objects.all()
        context["blog_recent"] = posts.order_by("-created_at")[:3]
        # context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.annotate(cat=Sum("categories")).order_by(
            "cat"
        )[:8]
        context["tags"] = Tag.objects.annotate(count1=Count(F("tags"))).filter(
            count1__gt=0
        )
        context["review_count"] = PostReview.objects.annotate(Count("post"))
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Post.objects.all()
        if self.request.method == "GET":
            req = self.request.GET
            if req.get("search"):
                queryset.filter(
                    Q(title__icontains=req.get["search"])
                    | Q(product__title__icontains=req.get["search"])
                    | Q(tag__title__icontains=req.get["search"])
                    | Q(author__get_full_name__icontains=req.get["search"])
                ).distinct
            if req.getlist("taglist"):
                queryset.filter(tag__slug__in=req.getlist("taglist")).distinct()
            if req.get("popular"):
                return queryset.annotate(count_review = Count('post')).order_by('-count_review')
            if req.get("category"):
                return queryset.filter(category__slug=req.get("category")).distinct()[
                    :10
                ]
            if req.get("tag"):
                return queryset.filter(tag__slug=req.get("tags")).distinct()[:7]
            if req.get("new_post"):
                return queryset.order_by("-created_at")
            if req.get("user"):
                user = (
                    User.objects.annotate(userid=Count("author"))
                    .filter(userid__gt=0)
                    .distinct
                )
            if req.get("author"):
                return queryset.filter(author__id=req.get("author"))
            return queryset


class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = "blog/blog_detail.html"
    form_class = PostReviewForm
    context_object_name = "post"
    slug_field = "slug"
    # slug_url_kwarg = 'slug'

    def get_success_url(self, **kwargs) -> str:
        if  kwargs != None:
            return reverse_lazy('blog:post', kwargs={'slug':self.get_object().slug })

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context["blog_recent"] = posts.order_by("-created_at")[:3]
        context["category"] = Category.objects.annotate(cat=Sum("categories")).order_by(
            "cat"
        )[:8]
        context["tags"] = Tag.objects.filter()
        context["tag_count"] = (
            context["tags"].annotate(count1=Count(F("tags"))).filter(count1__gt=0)
        )
        context["youmakelike"] = posts.all()[:2]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.id)
        print(self.request.user.id)
        form = self.get_form()
        if form.is_valid():
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        print('dfvgbnhjmhngbfvdfbgnhmhngbfvdvfbgn')
        form.instance.post=self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)