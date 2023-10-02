from core.utils import count_variant



def new_arrival(request):
   return count_variant.order_by('-created_at')[:8]