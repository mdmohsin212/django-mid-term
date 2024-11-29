from django.urls import path, include
from brand.views import *

urlpatterns = [
    path('', brand, name='brand'),
]