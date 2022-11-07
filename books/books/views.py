from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import  Q


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'  # this alternaticve for object_list for frontend works
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # login required permission


class BookDetailView(PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'  # our custom permission added here


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    # queryset = Book.objects.filter(title__icontains='odoo')

    # for searching
    def get_queryset(self):
        query = self.request.GET.get('q') #getting the name q
        return Book.objects.filter(
             Q(title__icontains=query) | Q(title__icontains=query)
        )
