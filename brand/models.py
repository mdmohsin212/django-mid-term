from django.db import models

# Create your models here.

class BrandModel(models.Model):
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.brand_name  