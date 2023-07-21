from django.db import models
from django.db.models.fields import EmailField, DateTimeField, CharField, TextField
# Create your models here.

class Subscriber(models.Model):
    email = EmailField(max_length= 50)                                                                                                                          

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Contact(models.Model):
    name = CharField(max_length=30)
    email = EmailField(max_length=50)
    phone = CharField(max_length=12, unique=True, verbose_name='Contact Phone')
    subject = CharField(max_length=50)
    message = TextField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

