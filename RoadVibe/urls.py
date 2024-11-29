from django.contrib import admin
from django.urls import path, include
from RoadVibe.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/<slug:category_slug>/', home, name='category_slug'),
    path('', include('author.urls')),
    path('car/', include('car.urls')),
    path('brand/', include('brand.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)