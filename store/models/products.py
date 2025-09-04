
from django.db import models

from store.models.shop import Shop

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField( max_digits = 10,
        decimal_places = 2)
    quantity_in_stock = models.IntegerField()
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    
