from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'phone', 'subject')
    list_display_links = ('name', 'email', 'phone', 'subject')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('name', 'email', 'phone', 'subject')


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')
    search_fields = ('email',)
    list_filter = ('email')


admin.site.register([Contact, Subscriber])


 