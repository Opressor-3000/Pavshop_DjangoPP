from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class DiscountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


class UnitAdmin(admin.ModelAdmin):    
    list_display = ('id', 'email')
    list_display_links = ('email')
    search_fields = ('email',)
    list_editable = ('email')
    list_filter = ('email')


admin.site.register([Product, Category, Discount, DiscountType, ProductReview, Store, Unit, Designer, Style, Brand, Collection])


