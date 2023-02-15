from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['categories', 'name', 'price', 'count_product', 'is_active']
    list_filter = ['categories', 'is_active']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'is_active']


class CategoriesBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']



admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CategoriesBlog, CategoriesBlogAdmin)