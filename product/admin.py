from django.contrib import admin


from mptt.admin import DraggableMPTTAdmin


from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'brand_id', 'collection_id', 'designer', 'price', 'publised_at', 'archive', 'user')
    list_display_links = ('title', 'brand_id', 'collection_id', 'designer', 'user')
    search_fields = ('title', 'price')
    list_editable = ('publised_at', 'archive',)
    list_filter = ('brand_id', 'category_id', 'style_id', 'collection_id', 'designer', 'price', 'archive')

class VariantImageInlines(admin.TabularInline):
    model = Image

class VariantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'product_id', 'price', 'color', 'unit', 'user')
    list_display_links = ('title',)
    search_fields = ('title', 'price', 'unit')
    list_editable = ('price',)
    list_filter = ('title', 'price', 'unit', 'product_id','discount_id', 'parent', 'user')
    inlines = (VariantImageInlines,)


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category_id',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category_id',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'type_id', 'code', 'amount', 'decrease_by', 'price_sum', 'other_product', 'discount_persent', 'date_begin', 'date_end', 'user', 'deleted_at')
    search_fields = ('pk', 'title', 'code', 'amount', 'decrease_by', 'price_sum', 'other_product', 'discount_persent', 'date_begin', 'date_end', 'user', 'deleted_at')
    list_filter = ('title', 'type_id', 'amount', 'decrease_by', 'price_sum', 'other_product', 'discount_persent', 'date_begin', 'date_end', 'user',)
    list_display_links = ('title',)
    list_editable = ('deleted_at',)


class DiscountTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'review', 'rating', 'published_at', 'deleted_at')
    list_display_links = ('review', 'product')
    search_fields = ('user', 'review', 'rating', 'product', 'published_at')
    list_editable = ('published_at',)
    list_filter = ('user', 'review', 'product', 'deleted_at', 'published_at')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'address', 'post', 'location', 'user', 'deleted_at')
    list_display_links = ('title',)
    search_fields = ('title', 'address', 'post', 'user', 'deleted_at')
    list_editable = ('deleted_at',)
    list_filter = ('title', 'address', 'post')


class UnitAdmin(admin.ModelAdmin):    
    list_display = ('pk', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)                      
    list_filter = ('title',)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title', 'user')
    list_display_links = ('title',)
    search_fields = ('title', 'user')
    list_filter = ('title', 'user')


class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


class DesignerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}
    list_display = ('pk', 'name', 'user')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'user')


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_display = ('pk', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['brand_id', 'title']}
    list_display = ('pk', 'title', 'brand_id', 'user')
    list_display_links = ['title']
    search_fields = ('title',)
    list_filter = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'user')
    list_display_links = ('user',)
    search_fields = ('user',)
    list_filter = ('image', 'user')


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

class VariantToStoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'variant', 'store', 'quantity')
    list_display_links = ('variant',)
    list_filter = ('variant', 'store')
    search_fields = ('quantity', 'variant', 'store')



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
admin.site.register(Tag, TagAdmin)
admin.site.register(VariantToStore, VariantToStoreAdmin)