from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField('Name',max_length=255, null=True, blank=True)
    address = models.CharField('Address',max_length=255, null=True, blank=True)
    acreage = models.CharField('Acreage',max_length=255, null=True, blank=True)
    link = models.CharField('Link_Image',max_length=255, null=True, blank=True)
    price = models.CharField('Price',max_length=255, null=True, blank=True)
    description = models.CharField('Description',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name