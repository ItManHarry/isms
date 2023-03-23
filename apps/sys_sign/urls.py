from django.urls import path
from . import  views
app_name = 'sys_sign'
urlpatterns = [
    path('login/', views.login, name='login'),
]