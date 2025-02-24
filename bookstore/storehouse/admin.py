from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_title', 
        'author', 
        'ISBN', 
        'quantity', 
        'user', 
        'created_date', 
        'modified_date',
    )
    list_filter = ('created_date', 'user')
    search_fields = ('book_title', 'author', 'ISBN', 'comments', 'user__username')
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': (
                'book_title', 
                'author', 
                'ISBN', 
                'quantity', 
                'comments', 
                'user',
            )
        }),
        ('Timestamps', {
            'fields': ('created_date', 'modified_date'),
        }),
    )

admin.site.register(Book, BookAdmin)
