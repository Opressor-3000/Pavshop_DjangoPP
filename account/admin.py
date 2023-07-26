from django.contrib import admin


from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'phone', 'email' )
    search_fields = ('email',)
    list_filter = ('email',)

class ProductBasketAdmin(admin.ModelAdmin):
    list_display = ('pk',  'user','variant', 'count')
    list_display_links = ('user', 'variant')
    search_fields = ('user', 'variant')
    list_filter = ('user', 'variant')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'company', 'address', 'city', 'country')
    list_display_links = ('company', 'address', 'city', 'country')
    search_fields = ('company', 'address', 'city', 'country')
    list_filter = ('user', 'company', 'address', 'city', 'country')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','status')
    list_display_links = ('pk', 'user','status')
    search_fields = ('user',)
    list_filter = ('user', 'status')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'variant')
    list_display_links = ('user', 'variant')
    search_fields = ('user', 'variant')
    list_filter = ('user', 'variant')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status')
    list_editable = ('email')


admin.site.register(User, AccountAdmin)
admin.site.register(ProductToBasket, ProductBasketAdmin)