from django.urls import path
from . import views
app_name = 'syscode'
urlpatterns = [
    path('wordbook/index/', views.wordbook_index, name='wordbook_index'),
    path('wordbook/add/', views.wordbook_add, name='wordbook_add'),
    path('wordbook/edit/<id>', views.wordbook_edit, name='wordbook_edit'),
    path('wordenum/add/<book_id>', views.wordenum_add, name='wordenum_add'),
    path('wordenum/edit/<book_id>/<enum_id>', views.wordenum_edit, name='wordenum_edit'),
]