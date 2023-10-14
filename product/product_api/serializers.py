from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from ..models import Category, Variant, Product, Tag, Brand, Style, Discount, DiscountType, Unit, Designer, Collection, VariantToStore, Store, Color


class CategorySerializer(ModelSerializer):
   serializer_related_field = SerializerMethodField()
   class Meta:
      model = Category
      fields = (
         'title',
         'parent',
      )

   def get_related_name_field(self, obj):
      pass


class TagSerializer(ModelSerializer):
   class Meta:
      model = Tag
      fields = (
         'title',
      )


class BrandSerializer(ModelSerializer):
   class Meta:
      model = Brand
      fields = {
         'title',
      }


class StyleSerializer(ModelSerializer):
   class Meta:
      model = Style
      fields = {
         'title',
      }


class CollectionSerializer(ModelSerializer):
   class Meta:
      model = Collection
      fields = {
         'title',
      }


class DesignerSerializer(ModelSerializer):
   class Meta:
      model = Designer
      fields = {
         'name',
      }


class DiscountTypeSerializer(ModelSerializer):
   class Meta:
      model = DiscountType
      fields = {
         'title'
      }


class DiscountSerializer(ModelSerializer):
   class Meta:
      model = Discount
      fields = {
         'title',
         'code',
         'type_id',
         'amount',
         'decrease_by',
         'price_sum',
         'other_product',
         'discount_persent',
         'date_begin',
         'date_end',
         'dalated_at'
      }


class UnitSerializer(ModelSerializer):
   class Meta:
      model = Unit
      fields = {
         'title'
      }


class ColorSerializer(ModelSerializer):
   class Meta:
      model = Color
      fields = {
         'title'
      }


class StoreSerializer(ModelSerializer):
   class Meta:
      model = Store
      fields = {
         'title',
         'address',
         'post',
         'location',
         'deleted_at',
      }


class ProductSerializer(ModelSerializer):
   tag = TagSerializer()
   category_id = CategorySerializer()
   brand_id = BrandSerializer()
   designer = DesignerSerializer()
   collection_id = CollectionSerializer()
   style_id = StyleSerializer()
   parent = PrimaryKeyRelatedField()
   class Meta:
      model = Product
      fields = (
         'title',
         'category_id',
         'price',
         'brand_id',
         'designer',
         'collection_id',
         'description',
         'style_id',
         'tag'
         'parent',   
         'published_at',
         'deleted_at',
      )

   def get_related_fields(self, model_field):
      return ProductSerializer()

class VariantSerializer(ModelSerializer):
   product_id = ProductSerializer()
   color = ColorSerializer()
   discount_id = DiscountSerializer()
   unit = UnitSerializer()
   tag = TagSerializer
   class Meta:
      model = Variant
      fields = (
         'title',
         'color',
         'product_id',
         'price',
         'discount_id',
         'unit',
         'tag',
         'parent',
         'in_stock',
      )


class VariantToStoreSerializer(ModelSerializer):
   variant = VariantSerializer()
   store = StoreSerializer()
   class Meta:
      model = VariantToStore
      fields = {
         'quantity'
      }
