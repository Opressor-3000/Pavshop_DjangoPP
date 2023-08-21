from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from .models import *

@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone", )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "saller",
                    "bloger",
                    "avatar",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ('username', 'first_name','last_name', 'saller', 'bloger', 'is_active', 'is_staff')
    list_display_links = ('username', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'username', 'phone', 'is_active', 'is_staff')
    list_filter = ('username', 'first_name', 'last_name', 'phone')
    list_editable = ('is_active', 'bloger', 'saller', )

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


# admin.site.register(User, AccountAdmin)
admin.site.register(ProductToBasket,ProductBasketAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(WishList, WishlistAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
