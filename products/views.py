from django.shortcuts import render
from products.models import *
from django.contrib import auth


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    username = auth.get_user(request).username
    return render(request, 'products/product.html', locals())
