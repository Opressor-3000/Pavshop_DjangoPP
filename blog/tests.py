from django.test import TestCase

# Create your tests here.
# OrderProduct.objects.filter(product=product).aggregate(... total=Sum(F('total_products'), output_field=IntegerField()) 
# {'total': 123}

# product_list = Product.objects.annotate(total_votes=Sum('vote__score')).order_by('total_votes')

# {{ car.date_of_manufacture|format_datetime }}
# {{ car.date_of_manufacture|format_datetime('full') }}