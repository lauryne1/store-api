
from django.db import models

from store.models.order import Order
from store.models.products import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()
    price = models.DecimalField( max_digits = 10,
        decimal_places = 2)
  
    
