from django.shortcuts import render
from django.views.generic import ListView
from .models import Publisher
class PublisherListView(ListView):
    model = Publisher
    template_name = 'books/publisher_list.html'
    # The context_object_name attribute on a generic view specifies the context variable to use:
    context_object_name = 'publisher_list'