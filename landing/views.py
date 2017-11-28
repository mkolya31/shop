from django.shortcuts import render
from .forms import SubcriberForm


def landing(request):
    name = 'Максим'
    form = SubcriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.save()

    return render(request, 'landing/landing.html', locals())

