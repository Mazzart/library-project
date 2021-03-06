from django.urls import path

from .views import BookList, BookDetail, CreateBook

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('create/', CreateBook.as_view(), name='add-book')
]