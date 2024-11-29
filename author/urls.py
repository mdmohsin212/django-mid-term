from django.urls import path, include
from author.views import *

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', user_login.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', show_profile, name='profile'),
    path('buy/<int:id>', buy_product.as_view(), name='buy'),
    path('profile/edit_profile', edit_profile, name='edit_profile'),
]