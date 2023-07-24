from django.db import models
from django.db.models.fields import EmailField, DateTimeField, CharField, TextField, BooleanField
# Create your models here.

class AbstractModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='create at')
    update_at=models.DateTimeField(auto_now=True, verbose_name='update at')

    class Meta:
        abstract=True

class Subscriber(AbstractModel):
    email = EmailField(max_length=50, unique=True, db_index=True, verbose_name='subscriber')

    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
        ordering = ['pk']                                                                                                                    


class Contact(AbstractModel):
    name = CharField(max_length=30, verbose_name='name')
    email = EmailField(max_length=50, verbose_name='email')
    phone = CharField(max_length=12, unique=True, verbose_name='Contact Phone')
    subject = CharField(max_length=50, verbose_name='subject')
    message = TextField(verbose_name='message')
    status = BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['-pk']