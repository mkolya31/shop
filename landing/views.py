from django.shortcuts import render, redirect
from django.contrib import auth
from products.models import ProductImage


def home(request):
    products_images = ProductImage.objects.filter(is_main=True)
    username = auth.get_user(request).username
    return render(request, 'landing/home.html', locals())
