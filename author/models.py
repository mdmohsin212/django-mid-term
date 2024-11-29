from django.db import models
from django.contrib.auth.models import User
from car.models import CarModel

# Create your models here.

class Authormodel(models.Model):
    buyer_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"buyer name {self.buyer_name} model {self.product}"