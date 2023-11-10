from django.db import models
from django.db.models.fields import EmailField, CharField, TextField, BooleanField
from django.urls import reverse_lazy


from .Abstact_models import AbstractModel
from account.models import User
from product.models import Variant


class Subscriber(AbstractModel):
    email = EmailField(max_length=50, unique=True, db_index=True, verbose_name='subscriber')

    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
        ordering = ['pk']

    def __str__(self) -> str:
        return str(self.email)                                                                                                     


class Contact(AbstractModel):
    name = CharField(max_length=30, verbose_name='name')
    email = EmailField(max_length=50, verbose_name='email')
    phone = CharField(max_length=12, unique=True, verbose_name='Contact Phone')
    subject = CharField(max_length=50, verbose_name='subject')
    message = TextField(verbose_name='message')
    status = BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['-pk']
    

class HomeSlider(AbstractModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='slider name')
    slide = models.ImageField(upload_to='slide_image/', verbose_name='slide')
    first_line = models.CharField(max_length=50, verbose_name='first line')
    second_line = models.CharField(max_length=50, verbose_name='second line')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, verbose_name='variant_in_slider')
    published_at = models.BooleanField(default=False)
    deleted_at = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    # class Meta:
    #     verbouse_name = 'slider'
    #     verbouse_name_plural = 'sliders'
    #     ordering = ['-pk']

    def __str__(self):
        return str(self.title)
    
    def get_absoluute_url(self):
        return reverse_lazy('homepage', kwargs={'slider': self.title })


