from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Book


def books_view(request):
    page_number = int(request.GET.get('page', 1))
    template = 'books/books_list.html'
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    page = paginator.get_page(page_number)
    context = {'books': page}

    return render(request, template, context)


def show_book(request, pub_date):
    template = 'base.html'
    books = Book.objects.filter(pub_date=pub_date).all()
    # date = pub_date.strftime('%Y-%m-%d')

    prev_date = Book.objects.filter(pub_date__lt=pub_date).first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).first()

    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date
            }

    return render(request, template, context)
