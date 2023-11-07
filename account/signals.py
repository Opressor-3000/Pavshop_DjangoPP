from django.db.models.signals import post_save, post_migrate, post_init, pre_save
from django.dispatch import receiver


from .models import ProductToBasket, Order, User
from .views import UserAccount


# @receiver(pre_save, sender=User,)
# def create_order(sender, instance, created, **kwargs):
#    pass

