from product.utils import count_variant



def new_arrival(request):
   return count_variant.filter(brand__variantofproduct__varianttostore__quantity__gt=0).distinct