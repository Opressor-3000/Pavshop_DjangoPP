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
    list_display = ('pk', 'order' , 'user', 'variant', 'count', 'discount_id')
    list_display_links = ('order', 'variant')
    search_fields = ('user', 'order', 'variant')
    list_filter = ('user', 'order', 'variant', 'count', 'discount_id')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'company_name', 'address', 'city', 'country')
    list_display_links = ('company_name', 'address')
    search_fields = ('company_name', 'address', 'city', 'country')
    list_filter = ('user', 'company_name', 'address', 'city', 'country')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','status', 'address')
    list_display_links = ('pk', 'user','status')
    search_fields = ('pk', 'user', 'address')
    list_filter = ('user', 'status', 'address')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'variant', 'deleted_at')
    list_display_links = ('user', 'variant')
    search_fields = ('user', 'variant')
    list_filter = ('user', 'variant', 'deleted_at')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('title',)


# admin.site.register(User, AccountAdmin)
admin.site.register(ProductToBasket,ProductBasketAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(WishList, WishlistAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
