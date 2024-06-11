from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones_objects = Phone.objects.all()

    if sort == 'name':
        context = {'phones': phones_objects.order_by('name')}
    elif sort == 'min_price':
        context = {'phones': phones_objects.order_by('price')}
    elif sort == 'max_price':
        context = {'phones': phones_objects.order_by('price').reverse()}
    else:
        context = {'phones': phones_objects}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone_object}

    return render(request, template, context)
