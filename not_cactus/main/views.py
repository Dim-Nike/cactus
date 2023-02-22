from django.shortcuts import render
from .models import *


def show_landing(req):
    data = {
        'name_page': 'Главная',
        'categories': Categories.objects.order_by('name'),
        'products': Product.objects.order_by('name'),
        'blogs': CategoriesBlog.objects.all()
    }
    return render(req, 'main/landing.html', data)


def show_list_products(req, pk):
    data = {
        'categories_contact': Categories.objects.order_by('name'),
        'categories': Categories.objects.filter(id=pk),
        'products': Product.objects.order_by('name'),
        'categories_blog_contact': CategoriesBlog.objects.all(),

    }
    return render(req, 'main/list_products.html', data)


def show_products(req, pk):
    data = {
        'categories_contact': Categories.objects.order_by('name'),
        'products': Product.objects.filter(id=pk),
        'popular_product': Product.objects.order_by('name'),
        'categories_blog_contact': CategoriesBlog.objects.all(),
    }
    return render(req, 'main/products.html', data)


def show_list_blog(req, pk):
    data = {
        'categories_contact': Categories.objects.order_by('name'),
        'categories_blog_contact': CategoriesBlog.objects.all(),
        'categories': CategoriesBlog.objects.filter(id=pk),
        'blogs': Blog.objects.all(),
        'popular_blog': Blog.objects.all(),
        'products_contact': Product.objects.order_by('name'),
    }

    return render(req, 'main/list_blog.html', data)


def show_blog(req, pk):
    data = {
        'blogs': Blog.objects.filter(id=pk),
        'popular_blog': Blog.objects.all(),
        'categories_contact': Categories.objects.order_by('name'),
        'product_contact': Product.objects.order_by('name'),
        'categories_blog_contact': CategoriesBlog.objects.all(),
    }

    return render(req, 'main/blog.html', data)


