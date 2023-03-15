from django.urls import path
from . import views
app_name = 'syscode'
urlpatterns = [
    path('wordbook/index/', views.wordbook_index, name='wordbook_index'),
    path('wordbook/add/', views.wordbook_add, name='wordbook_add'),
    path('wordbook/edit/<id>', views.wordbook_edit, name='wordbook_edit'),
]