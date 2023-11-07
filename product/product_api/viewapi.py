from rest_framework.generics import ListAPIView
from .serializers import VariantSerializer
from product.models import Variant
import django_filters.rest_framework

class VariantFilterAPIView(ListAPIView):
   queryset = Variant.objects.all()
   serializer_class = VariantSerializer
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields = ['product_id__category_id__slug']
   



