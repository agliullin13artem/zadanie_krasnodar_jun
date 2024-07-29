

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from simple_history.models import HistoricalRecords

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('L', 'Библиотекарь'),
        ('R', 'Читатель'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='R')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь.',
        verbose_name='группы'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Специфические разрешения для этого пользователя.',
        verbose_name='права пользователя'
    )

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    genre = models.CharField(max_length=255, verbose_name='Жанр')
    history = HistoricalRecords()

class BorrowRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    borrow_date = models.DateField(default=timezone.now, verbose_name='Дата выдачи')
    return_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')
    history = HistoricalRecords()

    def days_on_hand(self):
        if self.return_date:
            return (self.return_date - self.borrow_date).days
        return (timezone.now().date() - self.borrow_date).days
