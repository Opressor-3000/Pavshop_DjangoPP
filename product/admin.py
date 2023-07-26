from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"product_slug": ['title']}
    list_display = ('pk', 'title', 'price', 'views', 'archive')
    list_display_links = ('title', 'price', 'views', 'archive')
    search_fields = ('title', 'price')
    list_editable = ('price', 'archive')
    list_filter = ('title', 'price', 'views', 'archive')


class VariantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"variant_slug": ['title']}
    list_display = ('pk', 'title', 'price', 'quantity', 'unit')
    list_display_links = ('unit',)
    search_fields = ('title', 'price', 'quantity', 'unit')
    list_editable = ('price', 'quantity')
    list_filter = ('title', 'price', 'quantity', 'unit')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'parent')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('parent',)
    list_filter = ('parent',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'type_pk', 'sum', 'date_begin', 'date_end')
    list_display_links = ('type_pk',)
    search_fields = ('pk', 'title', 'sum', 'date_begin', 'date_end')
    list_editable = ('sum', 'date_begin', 'date_end')
    list_filter = ('pk', 'title', 'type_pk', 'sum', 'date_begin', 'date_end')


class DiscountTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'rating')
    list_display_links = ('user', 'product', 'publised_at')
    search_fields = ('user', 'product', 'published_at')
    list_editable = ('published_at',)
    list_filter = ('user', 'product', 'published_at')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')
    list_display_links = ('email',)
    search_fields = ('email',)
    list_editable = ('email',)
    list_filter = ('email',)


class UnitAdmin(admin.ModelAdmin):    
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(DiscountType, DiscountTypeAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Unit, UnitAdmin)