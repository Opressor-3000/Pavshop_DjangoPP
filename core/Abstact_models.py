from django.db import models


class AbstractModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='create at')
    update_at=models.DateTimeField(auto_now=True, verbose_name='update at')

    class Meta:
        abstract=True