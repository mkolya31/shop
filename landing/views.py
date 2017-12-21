from django.shortcuts import render
from .forms import SubcriberForm
from products.models import ProductImage


def landing(request):
    name = 'Максим'
    form = SubcriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_main=True)
    return render(request, 'landing/home.html', locals())
