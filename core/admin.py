from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')

admin.site.register(Contact)


 