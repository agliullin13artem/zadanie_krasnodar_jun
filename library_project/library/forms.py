
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Book, BorrowRecord

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book']
