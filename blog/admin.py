from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id')
    list_display_links = ('user_id')
    search_fields = ('user_id',)
    list_editable = ('user_id')
    list_filter = ('user_id')




admin.site.register([PostReview, Post])



