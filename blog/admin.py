from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'author', 'title', 'published_at')
    search_fields = ('author', 'title', 'published_at')
    list_editable = ('published_at', 'title')
    list_filter = ('author', 'published_at', 'title')


class PostReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'review')
    list_display_links = ('user', 'post', 'review')
    search_fields = ('user', 'post', 'review')
    list_filter = ('user',)


admin.site.register(PostReview, PostReviewAdmin)
admin.site.register(Post, PostAdmin)





