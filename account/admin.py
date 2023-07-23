from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


admin.site.register([User, Basket, Address, Order, WishList, Status])
