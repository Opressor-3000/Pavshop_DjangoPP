from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('id', 'user', 'product', 'title')
    list_display_links = ('user', 'product')
    search_fields = ('user', 'product', 'title')
    list_editable = ('product', 'title')
    list_filter = ('user', 'product', 'title')


class PostReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'review')
    list_display_links = ('user', 'post', 'review')
    search_fields = ('user', 'post', 'review')
    list_filter = ('user',)


admin.site.register(PostReview, PostReviewAdmin)
admin.site.register(Post, PostAdmin)





