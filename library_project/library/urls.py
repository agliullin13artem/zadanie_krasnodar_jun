

from django.urls import path
from . import views
from .api_views import BookListView, BorrowBookView, ReturnBookView

urlpatterns = [
     path('', views.book_list, name='book_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('my_books/', views.my_books, name='my_books'),
    path('debtors/', views.debtors_list, name='debtors_list'),

    # API routes
    path('api/books/', BookListView.as_view(), name='book-list-api'),
    path('api/borrow/', BorrowBookView.as_view(), name='borrow-book-api'),
    path('api/return/', ReturnBookView.as_view(), name='return-book-api'),
]
