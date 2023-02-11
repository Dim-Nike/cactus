from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path



urlpatterns = [
    path('', show_landing, name='landing'),
    path('products/<int:pk>', show_list_products, name='list_products'),
    path('product/<int:pk>', show_products, name='product'),
    path('test/', show_test, name='test'),
    path('index/', show_index, name='index')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)