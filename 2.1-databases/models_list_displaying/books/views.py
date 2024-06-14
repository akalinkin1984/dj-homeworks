from django.shortcuts import render, redirect

from .models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    data = []

    for book in books:
        data.append({'name': book.name,
                     'author': book.author,
                     'pub_date': book.pub_date.strftime('%Y-%m-%d')})

    context = {'books': data}

    return render(request, template, context)


def show_book(request, pub_date):
    template = 'base.html'
    books = Book.objects.filter(pub_date=pub_date).all()
    data = []

    for book in books:
        data.append({'name': book.name,
                     'author': book.author,
                     'pub_date': book.pub_date.strftime('%Y-%m-%d')})

    prev_date = Book.objects.filter(pub_date__lt=pub_date).first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).first()

    context = {
        'books': data,
        'prev_date': prev_date,
        'next_date': next_date
            }

    return render(request, template, context)
