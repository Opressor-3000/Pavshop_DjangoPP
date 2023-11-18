from django.db.models import (
    ForeignKey,
    CharField,
    SlugField,
    Sum,
    TextField,
    BooleanField,
    PROTECT,
    ImageField,
    ManyToManyField,
    Count,
)
from django.utils import timezone
from django.urls import reverse_lazy

from account.models import User
from product.models import Image, Tag, Category, Product
from core.Abstact_models import AbstractModel


class PostReview(AbstractModel):
    post = ForeignKey("Post", on_delete=PROTECT, related_name="post")
    user = ForeignKey(User, on_delete=PROTECT, related_name="userrew")
    text = TextField(verbose_name="review_text")
    review = ForeignKey(
        "self", on_delete=PROTECT, blank=True, null=True, related_name="postreviewrel"
    )
    deleted_at = BooleanField(default=False)

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ["pk"]

    def __str__(self) -> str:
        return str(self.id)


class Post(AbstractModel):
    title = CharField(max_length=100, unique=True, db_index=True, verbose_name="Title")
    slug = SlugField(max_length=100, unique=True, db_index=True)
    author = ForeignKey(
        User, on_delete=PROTECT, verbose_name="Author", related_name="author"
    )
    text = TextField(verbose_name="Content")
    preview = ImageField(upload_to="blog_image/", verbose_name="Preview")
    image = ManyToManyField(Image, blank=True, verbose_name="Image")
    published_at = BooleanField(default=False, verbose_name="Published at")
    tag = ManyToManyField(Tag, verbose_name="Tags", related_name="tags")
    category = ManyToManyField(
        Category, blank=True, verbose_name="About Categories", related_name="categories"
    )
    product = ManyToManyField(
        Product,
        blank=True,
        verbose_name="About Products",
        related_name="productsofpost",
    )
    deleted_at = BooleanField(default=False)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["created_at"]

    def get_absolute_url(self):
        return reverse_lazy("blog_detail", kwargs={"post": self.title})

    def __str__(self):
        return str(self.title)

    @property
    def get_review(self):
        review = PostReview.objects.filter(post=self.id)
        return review

    @property
    def get_reviewcount(self):
        return self.get_review.count()

    @property
    def get_author(self):
        return User.objects.filter(id=self.author)
    
    @property
    def get_categories(self):
        review = Category.objects.filter(id=self.category)
        return review
