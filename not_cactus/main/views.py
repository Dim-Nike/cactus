from django.shortcuts import render
from .models import *


def show_landing(req):
    data = {
        'name_page': 'Главная',
        'categories': Categories.objects.order_by('name'),
        'products': Product.objects.order_by('name'),
        'blogs': Blog.objects.order_by('name')
    }
    return render(req, 'main/landing.html', data)


def show_list_products(req, pk):
    data = {
        'categories': Categories.objects.filter(id=pk),
        'products': Product.objects.order_by('name')

    }
    return render(req, 'main/list_products.html', data)


def show_products(req, pk):
    data = {
        'products': Product.objects.filter(id=pk),
        'popular_product': Product.objects.order_by('name')
    }
    return render(req, 'main/products.html', data)

#
# def show_blog(req):
#     data = {
#         'blogs': Blog.objects.order_by('name')
#
#     }

