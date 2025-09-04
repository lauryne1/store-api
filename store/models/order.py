
from django.db import models

from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_amount = models.DecimalField( max_digits = 10,
        decimal_places = 2)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


