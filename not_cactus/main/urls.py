from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path



urlpatterns = [
    path('', show_landing, name='landing'),
    path('products/<int:pk>', show_list_products, name='list_products'),
    path('product/<int:pk>', show_products, name='product'),
    path('list_blog/<int:pk>', show_list_blog, name='list_blog'),
    path('blog/<int:pk>', show_blog, name='blog')
    # path('blog/', )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)