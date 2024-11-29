from django.shortcuts import render
from car.models import *
from brand.models import *

def home(request, category_slug=None):
    data = CarModel.objects.all()
    categories = BrandModel.objects.all()
    if category_slug is not None:
        try:
            category = BrandModel.objects.get(slug=category_slug)
            data = CarModel.objects.filter(brand=category)
        except BrandModel.DoesNotExist:
            data = CarModel.objects.none()
            
    return render(request, 'home.html', {'data' : data, 'catagory': categories}) 