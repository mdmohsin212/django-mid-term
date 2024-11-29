from django.urls import path, include
from car.views import *

urlpatterns = [
    path('detail/<int:id>/', details.as_view(), name='deatils_views'),
]