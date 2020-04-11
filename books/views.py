from django.views.generic import ListView, DetailView

from .models import Book


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
