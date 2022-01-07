from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(max_length=512)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
