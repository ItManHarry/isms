from django.urls import path
from .views import PublisherListView, PublisherDetailView, PublisherBookListView
app_name = 'view_gc'
urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name='publishers'),
    path('publisher/detail/<pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('books/<publisher>/', PublisherBookListView.as_view(), name='publisher_books'),
]