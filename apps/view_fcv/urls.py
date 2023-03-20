from django.urls import path
from . import views
app_name = 'view_fcv'
urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('author/', views.AuthorFormView.as_view(), name='author'),
]