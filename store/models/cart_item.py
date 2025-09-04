
from django.db import models

from store.models.cart import Cart
from store.models.products import Product


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()
