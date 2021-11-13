from django.db import models
from django.utils import timezone
from rest_framework.fields import ModelField
from setuptools import Command


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=70)
    telephone = models.CharField(max_length=12)
    class Meta:
        db_table = 'client'
        ordering=['name']
        
class Product(models.Model):
    label = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(name='stock',default=0)
    clients=models.ManyToManyField(Client,through='Command',through_fields=('product','client'))
    class Meta:
        db_table = 'product'
        ordering=['price']


        
class Command(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(name='quantity',default=1)
    date = models.DateField(default=timezone.now)
    class Meta:
        db_table = 'command'
        ordering=['date']