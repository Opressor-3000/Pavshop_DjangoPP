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
    list_filter = ('email',)



class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slide', 'first_line', 'second_line', 'variant', 'created_at', 'update_at', 'published_at')
    list_editable = ('title', 'slide', 'first_line', 'second_line', 'variant', 'published_at')
    list_filter = ('title', 'created_at', 'update_at', 'published_at')
    search_fields = ('title', 'variant', 'first_line', 'second_line')



admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(HomeSlider, HomeSliderAdmin)



 