from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    # print(type(str(books[0].pub_date)))
    return render(request, template, context)


def show_book(request, pub_date):
    template = 'base.html'
    books = Book.objects.filter(pub_date=pub_date).all()

    current_page = 'books/' + str(pub_date)
    paginator = Paginator(books, 10)
    page = paginator.get_page(current_page)

    # prev_date = Book.objects.filter(pub_date__lt=pub_date).first()
    try:
        prev_date = Book.objects.filter(pub_date__lt=pub_date).first()
    except:
        prev_date = None


    # next_date = Book.objects.filter(pub_date__gt=pub_date).first()
    try:
        next_date = Book.objects.filter(pub_date__gt=pub_date).first()
    except:
        next_date = None

    context = {
        'books': page,
        'prev_date': prev_date,
        'next_date': next_date
            }
    return render(request, template, context)
