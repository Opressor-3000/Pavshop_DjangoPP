from django.db import models

class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

class PostReview(models.Model):
    blog_id = models.ForeignKey('User', on_delete=models.PROTECT)

class PostImage(models.Model):
    blog_id = models.ForeignKey('User', on_delete=models.PROTECT)