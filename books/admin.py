from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('Book_name', 'Author_name','upload_date')
    
admin.site.register(Book,BookAdmin) 