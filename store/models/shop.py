from .store import Store
from django.db import models

from users.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
