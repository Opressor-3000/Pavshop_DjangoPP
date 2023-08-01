from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'price', 'views', 'archive')
    list_display_links = ('title', 'views')
    search_fields = ('title', 'price')
    list_editable = ('price', 'archive')
    list_filter = ('title', 'price', 'views', 'archive')


class VariantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'price', 'quantity', 'unit')
    list_display_links = ('unit',)
    search_fields = ('title', 'price', 'quantity', 'unit')
    list_editable = ('price', 'quantity')
    list_filter = ('title', 'price', 'quantity', 'unit')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'parent')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('parent',)
    list_filter = ('parent',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'type_id', 'sum', 'date_begin', 'date_end')
    search_fields = ('pk', 'title', 'sum', 'date_begin', 'date_end')
    list_editable = ('sum', 'date_begin', 'date_end')
    list_filter = ('title', 'type_id', 'sum', 'date_begin', 'date_end')


class DiscountTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'rating', 'published_at')
    list_display_links = ('user', 'product')
    search_fields = ('user', 'product', 'published_at')
    list_editable = ('published_at',)
    list_filter = ('user', 'product', 'published_at')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'address', 'post', 'location')
    search_fields = ('title', 'address', 'post')
    list_editable = ('title','address', 'post', 'location')
    list_filter = ('title', 'address', 'post')


class UnitAdmin(admin.ModelAdmin):    
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class DesignerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}
    list_display = ('pk', 'name')
    list_display_links = None
    search_fields = ('name',)
    list_editable = ('name',)
    list_filter = ('name',)


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title')
    list_display_links = None
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title', 'brand_id']}
    list_display = ('pk', 'title', 'brand_id')
    list_display_links = ['brand_id']
    search_fields = ('title',)
    list_editable = ('title',)
    list_filter = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image_url')
    list_display_links = None
    search_fields = ('image_url',)
    list_editable = ('image_url',)
    list_filter = ('image_url',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(DiscountType, DiscountTypeAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Designer, DesignerAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Collection, CollectionAdmin)