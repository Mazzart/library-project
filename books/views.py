from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')
