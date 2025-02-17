import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)

        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(list(reader), 10)
        page = paginator.get_page(page_number)

        context = {
             'bus_stations': page,
             'page': page,
        }

    return render(request, 'stations/index.html', context)
