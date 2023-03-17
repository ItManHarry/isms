from django.urls import path
from .views import PublisherListView
app_name = 'view_gc'
urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name='publishers'),
]