from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book
class PublisherListView(ListView):
    model = Publisher
    template_name = 'books/publisher_list.html'
    # The context_object_name attribute on a generic view specifies the context variable to use:
    context_object_name = 'publisher_list'
class PublisherBookListView(ListView):
    template_name = 'books/books_by_publisher.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        self.publisher = Publisher.objects.get(pk=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context

class PublisherDetailView(DetailView):
    template_name = 'books/publisher_detail.html'

    def get_queryset(self):
        self.publisher = Publisher.objects.get(pk=self.kwargs['pk'])
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context