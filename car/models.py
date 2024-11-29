from django.db import models
from brand.models import BrandModel
# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="cars")
    des = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
    