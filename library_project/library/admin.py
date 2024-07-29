

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import CustomUser, Book, BorrowRecord

class BookAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'genre')
    search_fields = ('title', 'author')

class BorrowRecordAdmin(SimpleHistoryAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')
    list_filter = ('user', 'book')
    search_fields = ('user__username', 'book__title')

admin.site.register(CustomUser)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
