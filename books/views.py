from django.shortcuts import render
from django.views.generic import ListView,DateDetailView
from .models import Book
from django.db.models import Q # ne
# Create your views here.

class BookListView(ListView):
    model = Book

    template_name = 'book_list.html'
    
class BookDetailView(DateDetailView):
    model = Book
    
    template_name = 'book_detail.html'
class SearchResultsListView(ListView): # new
    model = Book
    # context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    queryset = Book.objects.filter(title__icontains='beginners') # new
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
        )
