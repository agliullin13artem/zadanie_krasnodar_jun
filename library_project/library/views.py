

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, BookForm, BorrowForm
from .models import Book, BorrowRecord

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
    return render(request, 'login.html')

@login_required
def book_list(request):
    books = Book.objects.all().order_by('title')
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            BorrowRecord.objects.create(user=request.user, book=book)
            return redirect('book_list')
    else:
        form = BorrowForm()
    return render(request, 'book_list.html', {'books': books, 'form': form})

@login_required
def my_books(request):
    borrow_records = BorrowRecord.objects.filter(user=request.user)
    return render(request, 'my_books.html', {'borrow_records': borrow_records})

@login_required
def debtors_list(request):
    # Отбираем все записи о взятых книгах, у которых нет даты возврата
    borrow_records = BorrowRecord.objects.filter(return_date__isnull=True)
    return render(request, 'debtors.html', {'borrow_records': borrow_records})


def user_logout(request):
    logout(request)
    return redirect('user_login')
