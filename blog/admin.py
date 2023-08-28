from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'author', 'title', 'published_at', 'deleted_at')
    list_display_links = ('title', 'pk', 'author')
    search_fields = ('author', 'title',)
    list_editable = ('published_at', 'deleted_at')
    list_filter = ('author', 'published_at', 'deleted_at', 'title')


class PostReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'review', 'deleted_at')
    list_display_links = ('user', 'post', 'review')
    search_fields = ('user', 'post', 'review')
    list_filter = ('user', 'post', 'review')


admin.site.register(PostReview, PostReviewAdmin)
admin.site.register(Post, PostAdmin)





