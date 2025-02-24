from django.shortcuts import render
from .models import Book

# Create your views here.

from django.http import HttpResponse

def storehouse(request):
    items = Book.objects.all()
    return render(request, 'storehouse.html', {'items': items})


