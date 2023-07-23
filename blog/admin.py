from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id')
    list_display_links = ('user_id')
    search_fields = ('user_id',)
    list_editable = ('user_id')
    list_filter = ('user_id')


class PostReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


admin.site.register([PostReview, Post])



