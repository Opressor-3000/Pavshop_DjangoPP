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
    list_display = ('pk', 'user', 'company_name', 'address', 'city', 'country')
    list_display_links = ('company_name', 'address', 'city', 'country')
    search_fields = ('company_name', 'address', 'city', 'country')
    list_filter = ('user', 'company_name', 'address', 'city', 'country')


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
    list_display = ('pk', 'title')
    list_editable = ('title',)


admin.site.register(User, AccountAdmin)
admin.site.register(ProductToBasket,ProductBasketAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(WishList, WishlistAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
