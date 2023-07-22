from django.db import models
from django.db.models.fields import EmailField, DateTimeField, CharField, TextField
# Create your models here.

class AbstractModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)



    class Meta:
        abstract=True

class Subscriber(AbstractModel):
    email = EmailField(max_length= 50)                                                                                                                          

   


class Contact(AbstractModel):
    name = CharField(max_length=30)
    email = EmailField(max_length=50)
    phone = CharField(max_length=12, unique=True, verbose_name='Contact Phone')
    subject = CharField(max_length=50)
    message = TextField()

 