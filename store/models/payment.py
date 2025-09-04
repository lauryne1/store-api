from store.models.order import Order
from django.db import models


class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField( max_digits = 10,
        decimal_places = 2)
    status = models.CharField(max_length=100)

   
