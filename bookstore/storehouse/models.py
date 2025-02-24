from django.db import models
from accounts.models import Account

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    book_title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.CharField(max_length=10)
    ISBN = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    summary = models.TextField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.book_title
    

    